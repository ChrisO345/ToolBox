"""
directory_writer.py

This script generates the directory structure of the toolbox in Markdown format

"""

import os
from collections.abc import Iterator


def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    """
    A generator that yields the file paths for all the Python files in the directory

    Parameters
    ----------
    top_dir : str
              The directory to search for files in

    Yields
    ------
    str : The file path
    """
    for dir_path, dir_names, filenames in os.walk(top_dir):
        dir_names[:] = [
            d
            for d in dir_names
            if d != "scripts" and d[0] not in "._"
        ]
        for filename in filenames:
            if filename.startswith("__"):
                continue
            if os.path.splitext(filename)[1] in (".py", ".ipynb"):
                yield os.path.join(dir_path, filename).lstrip("./")


def md_prefix(i: int):
    """

    Parameters
    ----------
    i : int
        The number of spaces to indent

    Returns
    -------
    str
    """
    return f"{i * '  '}*" if i else "\n##"


def print_path(old_path: str, new_path: str) -> str:
    """
    Generates the Markdown for the new path

    Parameters
    ----------
    old_path : str
               The old path
    new_path : str
               The new path

    Returns
    -------
    new_path : str
               The new path
    """
    old_parts = old_path.split(os.sep)
    for i, new_part in enumerate(new_path.split(os.sep)):
        if (i + 1 > len(old_parts) or old_parts[i] != new_part) and new_part:
            if new_part.startswith("toolbox"):
                new_part = new_part[8:]
            print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")
    return new_path


def print_directory_md(top_dir: str = ".") -> None:
    """
    The function prints the directory structure in Markdown format

    Parameters
    ----------
    top_dir : str
              The directory to search for files in

    Returns
    -------
    None
    """
    old_path = ""
    for filepath in sorted(good_file_paths(top_dir)):
        filepath, filename = os.path.split(filepath)
        if filepath != old_path:
            old_path = print_path(old_path, filepath)
        indent = (filepath.count(os.sep) + 1) if filepath else 0
        url = f"{filepath}/{filename}".replace(" ", "%20")
        filename = os.path.splitext(filename.replace("_", " ").title())[0]
        print(f"{md_prefix(indent)} [{filename}]({url})")


if __name__ == "__main__":
    print_directory_md("toolbox/")
