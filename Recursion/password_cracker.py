#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(20000)
#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#
pwd_lst = []


def build_password(passwords, loginAttempt, i, cur_lst, checked):
    if checked[i]:
        return
    global pwd_lst
    if len(pwd_lst) > 0:
        # one of the path found a solution. Just need one, so stop here
        return
    if i > len(loginAttempt) - 1:
        pwd_lst = cur_lst[:]
        return
    for pwd in passwords:
        cur_str = loginAttempt[i:i + len(pwd)]
        if pwd == cur_str:
            cur_lst.append(pwd)
            build_password(passwords, loginAttempt, i + len(pwd), cur_lst, checked)
            cur_lst.pop()
    checked[i] = True


def quick_check(passwords, loginAttempt):
    # Quickly check to make sure all char in loginAttempt can be found in passwords
    pwd_all = "".join(passwords)
    for c in loginAttempt:
        if c not in pwd_all:
            return False
    return True


def passwordCracker(passwords, loginAttempt):
    if not quick_check(passwords, loginAttempt):
        return "WRONG PASSWORD"
    global pwd_lst
    checked = [False] * (len(loginAttempt) + 1)

    pwd_lst = []
    cur_lst = []
    build_password(passwords, loginAttempt, 0, cur_lst, checked)
    if len(pwd_lst) == 0:
        return "WRONG PASSWORD"
    return " ".join(pwd_lst)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt)

        fptr.write(result + '\n')

    fptr.close()
