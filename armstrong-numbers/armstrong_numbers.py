#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday, 17 July 2019 at 14:57:38

@author: vsanc
"""


def is_armstrong_number(number):
    if not isinstance(number, int):
        raise ValueError("Please enter an integer!")

    raised_to = len(str(number))
       
    return number == sum([int(x)**raised_to for x in str(number)]) 
