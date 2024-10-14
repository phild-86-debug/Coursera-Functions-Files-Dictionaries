# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 03:25:06 2024

@author: phild
"""

def add_em_up(nums: list[int])->int:
    assert type(nums) == list, "Parameter nums should be a list"
    for num in nums:
        assert type(num) == int or type(num) == float, "nums should contain only number values"
    tot = 0
    for num in nums:
        tot += num
    return tot

values = [2, 3.4, 17.87, 29]
print(add_em_up(values))