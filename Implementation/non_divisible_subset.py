#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # modulo count
    m_count = [0]*k

    # update m_count
    for i in s:
        m_count[i%k] += 1

    if k%2 == 0:
        m_count[int(k/2)] = min(m_count[int(k/2)], 1)

    res = min(m_count[0], 1)

    for i in range(1, (k//2)+1):
        res += max(m_count[i], m_count[k - i])

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
