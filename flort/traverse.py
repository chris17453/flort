from pathlib import Path
import logging
import os
from pathlib import Path
import logging
import os

def get_paths(
    directories=None, 
    extensions=None, 
    include_all=False, 
    include_hidden=False, 
    ignore_dirs=None
):
    """
    Traverses directories and collects paths with depth information.

    Args:
        directories (list): List of directories to traverse.
        extensions (list): List of file extensions to include.
        include_all (bool): Whether to include all files regardless of extension.
        include_hidden (bool): Whether to include hidden files.
        ignore_dirs (list): List of Path objects representing directories to ignore.

    Returns:
        list: A list of dictionaries containing path and depth information.
    """
    if directories is None or not directories:
        logging.error("No directories provided for traversal.")
        return []

    path_list = []
    ignore_dirs = ignore_dirs or []

    for base_directory in directories:
        base_path = Path(base_directory).resolve()
        parent_path = base_path.parent.resolve()

        if not base_path.is_dir():
            logging.error(f"The path {base_directory} is not a valid directory.")
            continue

        logging.info(f"Processing directory: {base_path}")

        if any(base_path == ignore_dir or ignore_dir in base_path.parents for ignore_dir in ignore_dirs):
            logging.info(f"Skipping ignored directory: {base_path}")
            continue

        path_list.append({
            "path": base_path, 
            "relative_path": str(base_path.relative_to(parent_path)), 
            "depth": 1, 
            'type': 'dir'
        })

        def scan_directory(current_path, current_depth):
            try:
                with os.scandir(current_path) as entries:
                    for entry in sorted(entries, key=lambda e: e.name):
                        entry_path = Path(entry.path)

                        # Skip hidden files/directories if not included
                        if not include_hidden and entry.name.startswith('.'):
                            continue

                        # Check if path should be ignored
                        if any(ignore_dir == entry_path or ignore_dir in entry_path.parents 
                              for ignore_dir in ignore_dirs):
                            logging.info(f"Skipping ignored path: {entry_path}")
                            continue

                        relative_path = entry_path.relative_to(parent_path)

                        if entry.is_dir():
                            path_list.append({
                                "path": entry_path,
                                "relative_path": str(relative_path),
                                "depth": current_depth,
                                'type': 'dir'
                            })
                            # Recursively scan subdirectories
                            scan_directory(entry_path, current_depth + 1)
                        elif entry.is_file():
                            if include_all or (extensions and entry_path.suffix.lower() in extensions):
                                path_list.append({
                                    "path": entry_path,
                                    "relative_path": str(relative_path),
                                    "depth": current_depth,
                                    'type': 'file'
                                })
            except PermissionError as e:
                logging.error(f"Permission denied accessing {current_path}: {e}")
            except Exception as e:
                logging.error(f"Error processing {current_path}: {e}")

        # Start recursive scan from base directory
        scan_directory(base_path, 2)  # Start depth at 2 since base dir is depth 1

    return path_list
