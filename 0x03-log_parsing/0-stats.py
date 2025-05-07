#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""

import sys

total_size = 0
status_counts = {}
valid_statuses = ['200', '301', '400', '401', '403', '404', '405', '500']
line_counter = 0


def print_stats():
    """Print accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        line_counter += 1
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        status_code = parts[-2]
        file_size = parts[-1]

        try:
            total_size += int(file_size)
        except ValueError:
            continue

        if status_code in valid_statuses:
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1

        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
