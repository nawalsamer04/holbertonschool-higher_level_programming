#!/usr/bin/python3
def safe_print_integer(value):
    """Print value as an integer. Return True if printed, else False."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
