#!/usr/bin/python3
"""
Reads stdin line by line and prints metrics:
- Total file size
- Count of status codes
Print every 10 lines and on keyboard interruption (CTRL+C).
"""

import sys

status_counts = {}
total_size = 0
line_count = 0
valid_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys(), key=int):
        print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        parts = line.split()

        # Parse size + status safely (ignore bad lines)
        if len(parts) >= 2:
            status = parts[-2]
            size = parts[-1]

            try:
                total_size += int(size)
            except Exception:
                pass

            if status in valid_codes:
                status_counts[status] = status_counts.get(status, 0) + 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

