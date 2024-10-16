from datetime import datetime
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 06:58:23 2024

@author: phild
"""

date_string = '1/1/2019'
format = '%m/%d/%Y'
date = datetime.strptime(date_string, format)
print(date)

print(date.year)
print(date.month)


