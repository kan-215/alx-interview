#!/usr/bin/python3

import sys

def display_metrics(status_counts, total_size):
    """
    Function to output metrics
    Args:
        status_counts: Dictionary of status codes and counts
        total_size: Cumulative file size
    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for key, count in sorted(status_counts.items()):
        if count != 0:
            print("{}: {}".format(key, count))


# Initialize cumulative size and counters
total_size = 0
status_code = 0
line_counter = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    # Read each line from standard input
    for line in sys.stdin:
        line_elements = line.split()  # Split by whitespace
        line_elements = line_elements[::-1]  # Reverse for easier access to last elements

        if len(line_elements) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_size += int(line_elements[0])  # Update total file size
                status_code = line_elements[1]  # Capture status code

                # Update count for valid status code if present
                if status_code in status_counts:
                    status_counts[status_code] += 1

            # Print every 10 lines
            if line_counter == 10:
                display_metrics(status_counts, total_size)
                line_counter = 0

finally:
    # Final output of metrics
    display_metrics(status_counts, total_size)

