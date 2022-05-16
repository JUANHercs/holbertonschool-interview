#!/usr/bin/python3
""" Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H
only ywo operations Copy All (*) and PAste (+)"""

def minOperations(n):
    count = 0
    if type(n) is not int or n <= 0:
        return(0)
    if n % 2 != 0:
        count = 1
    while n != 0:
        if n % 2:
            n = n // 2
            count += 1
        else:
            n -= 1
            count += 2
    return (count) 