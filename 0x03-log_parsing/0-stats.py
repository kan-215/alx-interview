#!/usr/bin/python3

import sys
from collections import defaultdict

def output_metrics(file_size_sum, status_counter):
    """
    Prints the accumulated file size and counts of each HTTP status code.
    
    Args:
        file_size_sum (int): Sum of all file sizes encountered.
        status_counter (dict): Dictionary holding count of each status code.
    """
    print("File size: {}".format(file_size_sum))
    for status in sorted(status_counter):
        if status_counter[status] > 0:
            print("{}: {}".format(status, status_counter[status]))

# Initialize counters and storage
file_size_sum = 0
status_counter = defaultdict(int)
line_count = 0
valid_status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}

try:
    for line in sys.stdin:
        # Split the input line into parts
        parts = line.split()
        
        # Verify the line format before processing
        if len(parts) >= 2:
            try:
                # Increment file size sum by the file size in this line
                file_size_sum += int(parts[-1])
                status_code = parts[-2]

                # Increment status counter if status code is valid
                if status_code in valid_status_codes:
                    status_counter[status_code] += 1
            except ValueError:
                # Ignore lines with non-integer file size
                continue
            
            # Track number of lines processed
            line_count += 1

            # Every 10 lines, output current metrics
            if line_count == 10:
                output_metrics(file_size_sum, status_counter)
                line_count = 0

except KeyboardInterrupt:
    # Print metrics if interrupted by Ctrl+C
    output_metrics(file_size_sum, status_counter)
    raise

# Final output for remaining lines
output_metrics(file_size_sum, status_counter)
