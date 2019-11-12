#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    h_str = d[h]
    h_next = d[h + 1] if h != 12 else "one"

    if m == 0:
        return h_str + " o' clock"
    elif m == 15:
        return "quarter past " + h_str
    elif m == 30:
        return "half past " + h_str
    elif m == 45:
        return "quarter to " + h_next
    elif m == 1:
        return "one minute past " + h_str
    elif m == 59:
        return "one minute to " + h_next
    elif m <= 20:
        return d[m] + " minutes past " + h_str
    elif m < 30:
        return "twenty " + d[m - 20] + " minutes past " + h_str
    else:
        m_tmp = 60 - m
        if m_tmp <= 20:
            return d[m_tmp] + " minutes to " + h_next
        elif m_tmp < 30:
            return "twenty " + d[m_tmp - 20] + " minutes to " + h_next


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
