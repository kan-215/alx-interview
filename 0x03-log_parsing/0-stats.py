#!/usr/bin/python3

import sys


def print_stats(status_counts, total_size):
    """
    Displays cumulative metrics based on log data.

    Args:
        status_counts (dict): Dictionary storing counts for each HTTP status code.
        total_size (int): Total accumulated file size from logs.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) > 6:
                # Extract the status code and file size
                status_code = parts[-2]
                file_size = parts[-1]

                # Update the total file size
                try:
                    total_size += int(file_size)
                except ValueError:
                    continue

                # Update the count for the status code if it's valid
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Increment the line count
                line_count += 1

                # Print metrics every 10 lines
                if line_count % 10 == 0:
                    print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise

    # Print final statistics after reading all lines
    print_stats(status_codes, total_size)
