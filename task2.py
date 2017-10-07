"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false.
"""

def isLucky(n):
    num_digits = len(str(n))
    print num_digits
    first_half_str = str(n)[0:num_digits/2]
    second_half_str = str(n)[num_digits/2:]
    sum_first_half = sum([int(i) for i in first_half_str])
    sum_second_half = sum([int(i) for i in second_half_str])
    if sum_first_half == sum_second_half:
        return True
    else:
        return False
    
    
