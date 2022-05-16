#!/usr/bin/python3
""" Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H
only ywo operations Copy All (*) and PAste (+)"""

def minOperations(n):

    if type(n) is not int or n <= 0:
        return 0

    count = 0
    letter = 1
    copy = 1

    while letter < n:
        if n % letter == 0:
            copy = letter
            count += 1
        if letter != n:
            letter += copy
            count += 1
        else:
            break

    return count