# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 08:06:49 2024

@author: phild
"""

# %% 4 A function that mirrors its string argument: forward and back
# =============================================================================
# #  4. write a function that mirrors its string argument, generating orginal and string backwards
# # Uses string slicing
# def mirror(mystr):
#     # your code here
#     return mystr + reverse(mystr)
# 
# def reverse(mystr):
#     return mystr[::-1]
# 
# str1 = input("Enter a string")
# print(mirror(str1))
# =============================================================================
    


# =============================================================================
# def ret_totals(num1, num2):
#     c = num1 + num2
#     return c
# result = ret_totals(5, 6)
# print(result)
# =============================================================================






# %% reverse string
# =============================================================================
# # Write a function that reverses it string argument
# def reverse(astring):
#     # your code here
#     new_string = ""
#     for char in astring:
#         new_string = char + new_string
#     return new_string
# 
# print(reverse("water comes from a fire hydrant!"))
# =============================================================================













# %% num_digits
# =============================================================================
# # function that will return the number of digits in a number
# def num_digits(num):
#     '''
#     input: integer value
#     output: num of digits in input
#     '''
#     count = 0
#     if num == 0:
#         return 1
#     else:
#         num = abs(num)
#         while int(num) > 0:
#             num = num / 10
#             count = count + 1   
#     return count
# 
# num1 = 1001
# print(num_digits(num1))
# =============================================================================





# %% num_test


# %% 5. removes all occurences of a letter from a given string
# =============================================================================
# def remove_letter(theLetter, theString):
#     # your code here
#     new_string = ""
#     if theLetter not in theString:
#         return theString
#     for char in theString:
#         if char == theLetter:
#             new_string = theString.replace(theLetter, "")
#     return new_string
# 
# str1 = input("Enter a string: ")
# print(remove_letter('t',str1))
# =============================================================================
            
            
            
            
            
# =============================================================================
# def num_test(num1):
#     ''' 
#     input- any number
#     output- greater, less than, or equal to 10
#     '''
#     
#     if num1 > 10:
#         return "Greater than 10."
#     elif num1 < 10:
#         return "Less than 10."
#     else:
#         return "Equal to 10."
# print(num_test(10))
# =============================================================================
    
    
    
    



# %% 6. Implement various list methods

# %%  6.1 count function


# =============================================================================
# # count, in, reverse, index, insert
# # count
# def count(char, str1):
#     count = 0
#     for letter in str1:
#         if letter == char:
#             count += 1 
#     return count
# 
#     
# str1 = input("Enter a string: ")
# char = input("Enter a single character: ")
# result = count(char, str1)           
# print(result)
# assert count(char, str1) == result
# =============================================================================

# %% 6.2 in function
    
# =============================================================================
# def my_in(values, items):
#     for item in values:
#         if item  == items:
#             return True
#           
#     return False
# 
# result = my_in([2, 3, 4, 9, 11, 17, 23], 3)
# print(result)
# =============================================================================
    
# %% 6.3 reverse function
""" # =============================================================================
def reverse(my_list):
    return my_list[::-1]

print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) """

    
    
    

 # %% 6.4 index function
# =============================================================================

""" def index(char, str1):
    for i in range(len(str1)):
        if str1[i] == char:
            return i
print(index('s', 'This is a test string.')) """



# %% 6.5 insert function
# =============================================================================
""" def insert(index, value, my_list):
    my_list.insert(index, value)
    return my_list
# print(insert(3, 'test', ['This', 'is', 'a', 'string.']))

# ============================================================================= """
   
# %% exercise 7
# function replace(s, old, new)

def replace(s, old, new):
    # your code here
    for char in s:
        if char == old:
            new_str = s.replace(old, new)
    return new_str
        
      # or char in theString:
      #         if char == theLetter:
      #             new_string = theString.replace(theLetter, "")
      #     return new_string      
        
print(replace("Mississippi", "i", "I"))
        
        
        
        