#!/usr/bin/python3
"""
Reads stdin line by line and prints metrics:
- File size: <total>
- <status_code>: <count>
Every 10 lines and on Ctrl+C (KeyboardInterrupt).
"""
import sys


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                # status code is usually second last, size is last
                try:
                    status = int(parts[-2])
                    size = int(parts[-1])
                    total_size += size
                    if status in status_counts:
                        status_counts[status] += 1
                except (ValueError, IndexError):
                    pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()

