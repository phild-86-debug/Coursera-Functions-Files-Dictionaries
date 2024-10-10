# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 05:08:37 2024

@author: owner
"""

# retrieve docstring in interpreter: hello__doc__
def hello():
    '''This functions says hello and greets you'''
    print("hello")
    print("Glad to meet you")
    
def add_list(alist):
    total = 0
    for num in alist:
        total += num
    return total



# non fruitfull function
def append_list(list1):
    list1.append('a')
    
def longer_than_five(list_of_names):
    names = list_of_names
    for name in names:
        if len(name) > 5:
            return True
    return False

    
# hello()


# my_list = [7, 3, 5, 4]
# print("Total sum is:", add_list(my_list))

# list2 = ['b', 'c', 'd']
# append_list(list2)
# print(list2)
# print(append_list(list2))

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))





