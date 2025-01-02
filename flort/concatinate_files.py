import os
from pathlib import Path
import logging
from datetime import datetime

from .utils import write_file



def concat_files(file_list,output):
    """
    Concatenates the contents of files from a provided file list,
    listing directories first and then files.

    Args:
        file_list (list): A list of dictionaries containing file paths and their depths.

    Returns:
        str: Concatenated contents of all directories and files.
    """
    dir_results = []
    file_results = []
    write_file(output,f"## File data\n")
    for item in file_list:
        file_path = item["path"]
        if file_path.is_file():  # Then process files
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    write_file(output,f"--- File: {item['relative_path']}\n{f.read()}\n")
                    
            except Exception as e:
                logging.error(f"Error reading file {file_path}: {e}")
                file_results.append(f"--- File: {file_path} ---\nError reading file.")

     
            

