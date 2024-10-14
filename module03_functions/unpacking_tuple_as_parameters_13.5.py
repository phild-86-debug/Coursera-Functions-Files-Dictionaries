# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 05:26:01 2024

@author: owner
"""

# unpack a tuple to use as a parameter in function

def add(x, y):
    return x + y
print(add(3, 4))
z = (5, 4)
print(add(*z))  # This line will lcause the values to be uppacked. 