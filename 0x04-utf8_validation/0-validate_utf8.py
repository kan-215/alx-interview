#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """
    the method determines if a given data set represents a valid
    UTF-8 encoding.
    """
    total_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for a in data:

        mask_byte = 1 << 7

        if total_bytes == 0:

            while mask_byte & a:
                total_bytes += 1
                mask_byte = mask_byte >> 1

            if total_bytes == 0:
                continue

            if total_bytes == 1 or total_bytes > 4:
                return False

        else:
            if not (a & mask_1 and not (a & mask_2)):
                    return False

        total_bytes -= 1

    if total_bytes == 0:
        return True

    return False
