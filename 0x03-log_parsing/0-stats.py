#!/usr/bin/python3

import sys


def print_metrics(dict_status, total_file_size):
    """
    Method to print
    Args:
        dict_status: dictionary of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


total_file_size = 0
code = 0
line_counter = 0
dict_status = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            line_counter += 1

            if line_counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_status.keys()):
                    dict_status[code] += 1

            if (line_counter == 10):
                print_metrics(dict_status, total_file_size)
                line_counter = 0

finally:
    print_metrics(dict_status, total_file_size)
