#!/usr/bin/env python3
"""
Flort - File Concatenation and Project Overview Tool

This module provides functionality to create a consolidated view of a project's
source code by combining multiple files into a single output file. It can generate
directory trees, create Python module outlines, and concatenate source files while
respecting various filtering options.

The tool is particularly useful for:
- Creating project overviews
- Generating documentation
- Sharing code in a single file
- Analyzing project structure

Usage:
    flort [DIRECTORY...] [--extension...] [options]

Example:
    flort . --py --js --output=project.txt --hidden
"""

import os
import argparse
import logging
from datetime import datetime
from pathlib import Path

from .utils import generate_tree, write_file,configure_logging,print_configuration
from .traverse import get_paths
from .concatinate_files import concat_files
from .python_outline import python_outline_files



def main() -> None:
    """
    Main entry point for the Flort tool.

    This function:
    1. Sets up argument parsing with detailed help messages
    2. Configures logging based on verbosity
    3. Processes command line arguments
    4. Generates the output file containing:
        - Directory tree (optional)
        - Python module outline (if requested)
        - Concatenated source files (unless disabled)

    Returns:
        None

    Raises:
        SystemExit: If required arguments are missing or invalid
    """
    output_file = f"{os.path.basename(os.getcwd())}.flort"
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create argument parser with comprehensive help
    parser = argparse.ArgumentParser(
        description="flort: create a single file of all given extensions, "
                   "recursively for all directories given. Ignores binary files.",
        prog='flort',
        add_help=False,
        prefix_chars='-',
        allow_abbrev=False
    )

    # Define command-line arguments with detailed help messages
    parser.add_argument('directories',   metavar='DIRECTORY',  help='Directories to list files from, defaults to the current working directory.',default=".",type=str,nargs='*')
    parser.add_argument('-h', '--help',  action='help',        help='Show this help message and exit.')
    parser.add_argument('--ignore-dirs', type=str,             help='Directories to ignore (comma-separated list).')
    parser.add_argument('--output',      type=str,             help='Output file path. Defaults to the basename of the current directory '             'if not specified. "stdio" will output to console.' ,default=output_file)
    parser.add_argument('--outline',     action='store_true',  help='Create an outline of the files instead of a source dump.')
    parser.add_argument('--no-dump',     action='store_true',  help='Do not dump the source files')
    parser.add_argument('--no-tree',     action='store_true',  help='Do not print the tree at the beginning.')
    parser.add_argument('--all',         action='store_true',  help='Include all files regardless of extensions.')
    parser.add_argument('--hidden',      action='store_true',  help='Include hidden files.')
    parser.add_argument('--verbose',     action='store_true',  help='Enable verbose logging (INFO level).')


    # Parse known args, allowing unknown args for extensions
    args, unknown_args = parser.parse_known_args()

    # Configure logging based on verbosity flag
    configure_logging(args.verbose)

    # Process ignore_dirs argument
    if args.ignore_dirs:
        ignore_dirs = [Path(ignore_dir).resolve() 
                      for ignore_dir in args.ignore_dirs.split(',')]
    else:
        ignore_dirs = []

    # Process extensions from unknown arguments
    extensions = [f".{ext.lstrip('-')}" for ext in unknown_args 
                 if ext.startswith('--')]

    # Log configuration settings
    print_configuration(
        args.directories,
        extensions,
        args.all,
        args.hidden,
        ignore_dirs
    )

    # Validate extensions or --all flag
    if not extensions and not args.all:
        logging.error("No extensions provided and --all flag not set. "
                     "No files to process.")
        return

    # Initialize output file with timestamp
    write_file(args.output, f"## Florted: {current_datetime}\n", 'w')

    # Get list of files to process
    path_list = get_paths(
        args.directories,
        extensions=extensions,
        include_all=args.all,
        include_hidden=args.hidden,
        ignore_dirs=ignore_dirs
    )

    print(f"Output to {args.output}\n")

    # Generate directory tree if not disabled
    if not args.no_tree:
        generate_tree(path_list, args.output)

    # Generate Python outline if requested
    if args.outline:
        python_outline_files(path_list, args.output)
    
    # Concatenate source files if not disabled
    if not args.no_dump:
        concat_files(path_list, args.output)


if __name__ == "__main__":
    main()