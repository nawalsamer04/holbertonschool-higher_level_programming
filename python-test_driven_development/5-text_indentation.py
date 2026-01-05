#!/usr/bin/python3
"""Module that defines text_indentation."""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): input text

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = ""
    for ch in text:
        buf += ch
        if ch in ".?:":
            print(buf.strip(), end="\n\n")
            buf = ""

    if buf:
        print(buf.strip(), end="")
