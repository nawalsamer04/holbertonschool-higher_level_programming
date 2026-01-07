#!/usr/bin/env python3
"""
Task 2 - Converting CSV Data to JSON Format
Read a CSV file and write its content to data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and write to 'data.json'.

    Args:
        csv_filename (str): Input CSV filename.

    Returns:
        bool: True if conversion succeeded, False otherwise (ex: file not found).
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as out:
            json.dump(rows, out)

        return True
    except FileNotFoundError:
        return False
    except (OSError, csv.Error, TypeError, ValueError):
        return False
