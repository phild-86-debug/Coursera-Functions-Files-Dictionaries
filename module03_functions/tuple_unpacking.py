# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 04:52:54 2024

@author: phild
"""
# The pythonic way to enumerate items in a sequence

# One method using range
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])
print('\n')

print("Using the enumerate method: ")
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])
    
print('\n')
print("The best method to consume the results of enumerate")
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)




print("----------------------------------------------")
print('\n\n')
# swapping variables
a = 1
b = 2
a, b = b, a
print(a, b)

authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)