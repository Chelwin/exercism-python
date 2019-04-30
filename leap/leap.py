#!/usr/bin/env python3
# -* coding:utf-8 -*-
"""
Created on Sunday, 28 April 2019 at 14:36:57

@author: vsanc
"""


def is_leap_year(year):
    if not isinstance(year, int):
        raise ValueError("Please enter an integer!")

# A leap year must follow  at least (logical OR) one of the two paths:
#    Be divisible by 400; i.e. by 4 AND 100
#    Be divisible by 4; i.e. by 4 AND NOT 100
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# TEST SUITE #
data = []
true = []
file_name = "leap.in"

try:
    fh = open(file_name, 'r')
except IOError:
    print("Cannot open", file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')   # remove trailing new line char
#            print(addIt)
            data.extend(addIt)
#   print(data)
finally:
    fh.close()

if data:
    for year in data:
        true.append(is_leap_year(int(year)))

print(all(true))   # if all leap years are detected correctly, prints True
