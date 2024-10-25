#!/usr/bin/python3

import sys


def print_msg(dict_st, total_size):
    """
    function to print
    Args:
        dict_st: dictionary of status codes
        total_size: totalsize
    Returns:
        Nothing
    """

    print("File size: {}".format(total_size))
    for key, val in sorted(dict_st.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
code = 0
counter = 0
dict_st = {"200": 0,
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
            counter += 1

            if counter <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in dict_st.keys()):
                    dict_st[code] += 1

            if (counter == 10):
                print_msg(dict_st, total_size)
                counter = 0

finally:
    print_msg(dict_st, total_size)
