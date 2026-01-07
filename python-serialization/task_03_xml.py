#!/usr/bin/env python3
"""
Task 3: Serializing and deserializing a dictionary using XML.
"""

import xml.etree.ElementTree as ET


def _to_best_type(value):
    """Convert string values back into bool/int/float when possible."""
    if value is None:
        return ""

    v = value.strip()

    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False

    # int
    try:
        if v.isdigit() or (v.startswith("-") and v[1:].isdigit()):
            return int(v)
    except Exception:
        pass

    # float
    try:
        return float(v)
    except Exception:
        return v


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save to `filename`.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML from `filename` and return a reconstructed Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = _to_best_type(child.text)

    return result

