#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on Sunday, 28 April 2019 at 14:36:57

@author: vsanc
"""


#def is_leap_year(year):
#    if not isinstance(year, int):
#        raise ValueError("Please enter an integer")
#
#    return year%4 == 0 and (year%100 != 0 or year%400 == 0)




def is_leap_year(year):
    leap = False
    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        leap = False
    elif year%4 == 0:
        leap = True
    return leap



data = []
true = []
file_name = "leap.in"

try:
   fh = open(file_name, 'r')
except IOError:
   print("Cannot open",file_name)
else:
   for new in fh:
       if new != '\n':
           addIt = new[:-1].split(',')   # remove trailing new line char
#           print(addIt) 
           data.extend(addIt)
#   print(data)
finally:
   fh.close() 

if data:
    for year in data:
        true.append(is_leap_year(int(year)))

print(all(true))   # check if all leap years are detected correctly, prints True

