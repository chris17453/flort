"""
File Utilities Module

This module provides utility functions for file operations including:
- Binary file detection
- Content cleaning
- File writing
- Directory tree generation

These utilities support the core functionality of the file processing system
while handling errors gracefully and providing appropriate logging.
"""

import os
import argparse
from pathlib import Path
import logging
from datetime import datetime


def is_binary_file(file_path: Path) -> bool:
    """
    Determine if a file is binary by examining its contents.

    Args:
        file_path (Path): Path to the file to check

    Returns:
        bool: True if the file appears to be binary, False otherwise

    The function uses two methods to detect binary files:
    1. Checks for null bytes in the first 1024 bytes
    2. Looks for non-text characters outside the ASCII printable range

    Note:
        - Returns True on any error, assuming binary to be safe
        - Only reads the first 1024 bytes for efficiency
    """
    try:
        with open(file_path, 'rb') as file:
            # Read first chunk of file
            chunk = file.read(1024)
            
            # Quick check for null bytes
            if b'\x00' in chunk:
                return True
                
            # Check for non-text characters
            text_characters = bytes(range(32, 127)) + b'\n\r\t\f\b'
            return bool(chunk.translate(None, text_characters))
            
    except Exception as e:
        logging.error(f"Error determining if file is binary {file_path}: {e}")
        return True


def clean_content(file_path: Path) -> str:
    """
    Clean up file content by removing unnecessary whitespace.

    Args:
        file_path (Path): Path to the file to clean

    Returns:
        str: Cleaned content with empty lines removed and remaining lines stripped

    The function:
    1. Reads all lines from the file
    2. Strips whitespace from each line
    3. Filters out empty lines
    4. Joins remaining lines with newlines

    Note:
        - Preserves line breaks between non-empty lines
        - Removes leading/trailing whitespace from each line
        - Removes completely empty lines
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        cleaned_lines = [line.strip() for line in lines if line.strip()]
        return '\n'.join(cleaned_lines)


def write_file(file_path: str, data: str, mode: str = 'a') -> None:
    """
    Write data to a file or output to console.

    Args:
        file_path (str): Path to output file or "stdio" for console output
        data (str): Content to write
        mode (str, optional): File opening mode ('w' for write, 'a' for append).
            Defaults to 'a'.

    The function handles two output modes:
    1. File output: Writes to the specified file path
    2. Console output: Prints to stdout if file_path is "stdio"

    Error handling:
    - IOError: Logged with specific error message
    - Other exceptions: Logged with generic error message

    Note:
        - Creates parent directories if they don't exist
        - Logs success with mode information
        - Handles both creation and append operations
    """
    try:
        if file_path == "stdio":
            print(data)
        else:
            # Create parent directories if they don't exist
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, mode) as file:
                file.write(data)
            
            operation = 'create' if mode == 'w' else 'append'
            logging.info(f"Output written to: {file_path}. Mode: {operation}.")
            
    except IOError as e:
        logging.error(f"Failed to write to {file_path}: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while writing to {file_path}: {e}")


def generate_tree(path_list: list, output: str) -> None:
    """
    Generate a hierarchical tree structure from a list of paths.

    Args:
        path_list (list): List of dictionaries containing path information with keys:
            - 'path': Path object
            - 'depth': Integer depth in tree
            - 'type': String indicating 'dir' or 'file'
        output (str): Path to output file where tree will be written

    The function:
    1. Writes a header to the output
    2. Processes each path in the list
    3. Creates appropriate indentation based on depth
    4. Formats directories with trailing slash
    5. Writes the formatted tree to the output

    Tree format example:
    ## Directory Tree
    root/
    |-- dir1/
    |   |-- file1.txt
    |   |-- file2.txt
    |-- dir2/
        |-- subdir/
            |-- file3.txt

    Note:
        - Directories end with '/'
        - Indentation uses '|-- ' for items and '|   ' for depth
        - Tree structure shows hierarchical relationships
    """
    write_file(output, "## Directory Tree\n")
    structure = []

    for item in path_list:
        path = item["path"]
        depth = item["depth"]
        indent = '|   ' * (depth - 1) + '|-- ' if depth > 0 else ''
        
        if item['type'] == 'dir':
            structure.append(f"{indent}{path.name}/")
        elif item['type'] == 'file':
            structure.append(f"{indent}{path.name}")
    
    write_file(output, '\n'.join(structure))


def configure_logging(verbose: bool) -> None:
    """
    Configure the logging system based on the verbosity level.

    Args:
        verbose (bool): If True, sets logging level to INFO;
                       if False, sets it to WARNING.

    The logging format includes timestamp, level, and message:
        2024-01-02 12:34:56 - INFO - Sample message
    """
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def print_configuration(
    directories: list,
    extensions: list,
    include_all: bool,
    include_hidden: bool,
    ignore_dirs: list = None
) -> None:
    """
    Log the current configuration settings for the file processing operation.

    Args:
        directories (list): List of directory paths to process
        extensions (list): List of file extensions to include
        include_all (bool): Whether to include all file types
        include_hidden (bool): Whether to include hidden files
        ignore_dirs (list, optional): List of directories to ignore

    This function provides visibility into the tool's configuration,
    which is particularly useful for debugging and verification.
    """
    logging.info(f"Processing: {', '.join(directories)}")
    logging.info(f"Types: {', '.join(extensions)}")
    logging.info(f"All files: {include_all}")
    logging.info(f"Hidden files: {include_hidden}")
    if ignore_dirs:
        for dir in ignore_dirs:
            logging.info(f"Omitting: {dir}")
