# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:03:53 2024

@author: owner
"""

'''  Instructions

Provided is a list of data about a store’s inventory
 where each item in the list represents the name of an item,
 how much is in stock, and how much it costs.
 Print out each item in the list with the same formatting,
 using the .format method (not string concatenation). 
 For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
'''


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

# task 1 need to split inventory into parts
for product in inventory:
    print(product.strip().split())
    
# Assign the split into a varaible
for product in inventory:
    line = product.strip().split(',')   
    product = line[0]
    quantity = line[1]
    cost = line[2]
    
    # format the string
    print("The store has{} {}, each for{} USD.".format(quantity, product, cost))
    

    
    
