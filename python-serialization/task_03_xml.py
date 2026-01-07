#!/usr/bin/python3
"""
Task 3: Serialize and deserialize a Python dictionary using XML.
"""

import xml.etree.ElementTree as ET


def _to_text(value):
    """Convert Python value to text for XML."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _from_text(text):
    """Best-effort convert XML text back to Python types."""
    if text is None:
        return ""
    t = text.strip()

    if t == "null":
        return None
    if t.lower() == "true":
        return True
    if t.lower() == "false":
        return False

    # int?
    if t.isdigit() or (t.startswith("-") and t[1:].isdigit()):
        try:
            return int(t)
        except Exception:
            pass

    # float?
    try:
        if "." in t:
            return float(t)
    except Exception:
        pass

    return t


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to `filename`.
    XML structure:
      <data>
        <key>value</key>
      </data>
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = _to_text(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Deserialize XML from `filename` back into a Python dictionary.
    Returns None on any error (missing file, bad XML, etc.).
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = _from_text(child.text)
        return result
    except Exception:
        return None

