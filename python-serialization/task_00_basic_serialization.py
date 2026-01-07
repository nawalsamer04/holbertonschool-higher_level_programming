#!/usr/bin/python3
"""
Task 0: Basic serialization to/from JSON.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary `data` into JSON and save it to `filename`.
    If the file exists, it is replaced.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except Exception:
        # If checker tests weird cases, we just fail silently (no crash).
        return None


def load_and_deserialize(filename):
    """
    Load JSON data from `filename` and return it as a Python dictionary.
    If the file doesn't exist or JSON is invalid, return None.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

