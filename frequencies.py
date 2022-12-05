"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for x in items:
        if str(x) in frequencies:
            frequencies[str(x)] = frequencies[str(x)]+1
        else:
            frequencies[str(x)]=1
    return frequencies
