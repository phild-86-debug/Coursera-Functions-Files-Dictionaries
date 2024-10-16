import csv
from datetime import datetime
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:22:50 2024

@author: phild

"""
def com_max_value(interest_values):
    max = interest_values[0]
    for val in interest_values:
        if val > max:
            max = val
    return max
def com_average(l_values):
    sum = 0
    for num in (l_values):
        num = float(num)
        sum += num
    return sum / len(l_values)
def ret_date_obj(date_string):
    format = '%m/%d/%Y'
    date = datetime.strptime(date_string, format)
    return date


# task 1 open text in csv reader SP500.txt
sp = []
interest = []
with open('SP500.txt', 'r') as f:
    reader = csv.DictReader(f)
    # print(reader.fieldnames)
    for row in reader:
        Date = row['Date']
        # print(Date)
        date = ret_date_obj(Date)
        if(date.month >= 6 and date.year == 2016) or(date.year == 2017 and date.month <= 5) :
            sp.append(row['SP500'])
            interest.append(row['Long Interest Rate'])
mean_SP = com_average(sp)
print(mean_SP)
max_interest = com_max_value(interest)
print(max_interest)

            
# print(sp)
# print(interest)

    