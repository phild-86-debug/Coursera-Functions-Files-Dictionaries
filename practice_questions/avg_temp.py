# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:05:58 2024

@author: owner
"""

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
temps = week_temps_f.split(",")
sum_temps = 0

for temp in temps:
    sum_temps += float(temp)
avg_temp = sum_temps/len(temps)
print(avg_temp)
