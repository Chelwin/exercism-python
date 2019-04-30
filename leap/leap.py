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
