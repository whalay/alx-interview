#!/usr/bin/python3
""" This module contains a function that return the number of minimum operation"""


def minOperations(n):
    """
        return the minimum number of 
        operations to be carried out
    """
    if n <= 1:
        return 0

    # Initialize variables
    operations = [0] * (n + 1)

    # Calculate the minimum operations needed for each value up to n
    for i in range(2, n + 1):
        # Initialize with a high value to find the minimum
        operations[i] = float('inf')

        # Try all possible factors of i and calculate the minimum
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))

    return operations[n]
