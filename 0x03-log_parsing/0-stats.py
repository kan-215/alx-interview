#!/usr/bin/python3

import sys


def print_stats(status_counts, total_size):
    """
    Function to print cumulative log statistics.

    Args:
        status_counts (dict): Dictionary holding status code counts.
        total_size (int): Sum of all log file sizes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) > 6:
                # Parse and update the status code and file size
                status_code = parts[-2]
                file_size = parts[-1]

                # Update total file size
                try:
                    total_size += int(file_size)
                except ValueError:
                    continue

                # Update status code count if valid
                if status_code in status_codes:
                    status_codes[status_code] += 1

                # Increment line count
                line_count += 1

                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise

    # Final stats output after stdin completes
    print_stats(status_codes, total_size)
