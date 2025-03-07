"""
read_env.py

Author: Chris Oliver
Date: 08/08/2024
"""

import csv
from typing import Mapping, TypedDict
# TODO: Tidy this and fix

def read_env(path: str) -> Mapping[str, str]:
    """
    Read the .env file and return the key-value pairs.

    Parameters
    ----------
    path : str
           The path to the .env file.

    Returns
    -------
    Mapping[str, str]
        A dictionary containing the key-value pairs from the .env file.
    """
    with open(path, 'r') as file:
        reader = csv.reader(file)
        env_dict = {}
        for row in reader:
            key, val = row[0].split('=')
            env_dict.update({key: val.strip('"')})
    return env_dict


if __name__ == '__main__':
    print(read_env("text.env"))
