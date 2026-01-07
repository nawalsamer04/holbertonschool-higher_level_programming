#!/usr/bin/env python3
"""
Task 0 - Basic Serialization
Serialize a Python dictionary into a JSON file and deserialize it back.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary `data` to JSON and save it to `filename`.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON filename. If it exists, it is replaced.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except (TypeError, OSError):
        # TypeError: data not JSON serializable
        # OSError: file issues (permissions, etc.)
        pass


def load_and_deserialize(filename):
    """
    Load JSON data from `filename` and return it as a Python dictionary.

    Args:
        filename (str): Input JSON filename.

    Returns:
        dict: Deserialized dictionary, or None if file can't be read/decoded.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None

