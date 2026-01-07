#!/usr/bin/python3
"""Module that inserts a line of text after each line containing a string."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert `new_string` in the file after each line containing `search_string`.

    Args:
        filename (str): path to the file
        search_string (str): string to search for in each line
        new_string (str): string to insert after matching lines
    """
    lines_out = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines_out.append(line)
            if search_string in line:
                lines_out.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines_out)

