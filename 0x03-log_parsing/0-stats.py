#!/usr/bin/python3

import sys

def print_metrics(total_file_size, status_code_counts):
    """
    Print the total file size and count of each status code.
    
    Args:
        total_file_size (int): Sum of all file sizes.
        status_code_counts (dict): Dictionary with status codes as keys and their counts as values.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

# Initialize variables
total_file_size = 0
line_count = 0
status_code_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

try:
    for line in sys.stdin:
        parts = line.split()

        # Check if line format is valid
        if len(parts) < 7:
            continue
        try:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status code count if it's one of the tracked codes
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_file_size, status_code_counts)

        except (ValueError, IndexError):
            # Skip lines with parsing errors
            continue

except KeyboardInterrupt:
    # On interruption, print the final metrics
    pass
finally:
    # Print the metrics at the end of the input
    print_metrics(total_file_size, status_code_counts)
