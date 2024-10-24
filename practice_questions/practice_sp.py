# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:49:11 2024

@author: owner
"""

filename = 'SP500.txt'
l_interest = []
l_sp = []

with open(filename, 'r') as f:
    lines = f.readlines()[6:18]
    for lin in lines:
        num_lines = len(lines)
        row = lin.split(',')
        l_interest.append(row[5])
        l_sp.append(row[1])

max_interest = float(max(l_interest))


print(max_interest)
sum = 0  
for num in l_sp:
    sum = sum + float(num)
mean_SP = (sum)/len(lines)
print(mean_SP)

     
        
        
        
        
    
