#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Function to output the current metrics.
    Args:
        dict_sc: dictionary storing status codes and their counts
        total_file_size: cumulative file size
    Returns:
        None
    """
    
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize total file size and counters
total_file_size = 0
code = 0
counter = 0
dict_sc = {
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
    # Read input line by line
    for line in sys.stdin:
        parsed_line = line.split()  # Split line into components
        parsed_line = parsed_line[::-1]  # Reverse list for easier indexing

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # Add file size
                code = parsed_line[1]  # Capture status code

                # Update count for existing status code
                if code in dict_sc.keys():
                    dict_sc[code] += 1

            # Every 10 lines, display current stats
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

except KeyboardInterrupt:
    # Print metrics on interruption (Ctrl+C)
    print_msg(dict_sc, total_file_size)
