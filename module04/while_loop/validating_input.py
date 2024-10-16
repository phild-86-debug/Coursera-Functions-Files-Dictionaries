# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 07:04:07 2024

@author: owner
"""
# This is also a form of the listener loop
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper()
        if answer ==  'Y' or answer == 'N':
            valid_input = True
    return answer

response = get_yes_or_no("Do you like lima beans? Y)es or N)o: ")
if response == 'Y':
    print("Great, they are very healthy.")
else:
    print("Too bad. If cooked right, they are quite tasty.")
    
    