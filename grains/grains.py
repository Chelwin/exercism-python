#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, 7 May 2019 at 20:42:50

@author: vsanc
"""


def on_square(integer_number):
    """ Calculate the square of a number between 1 & 64 (both inclusive).
    """
    if (integer_number < 1 or integer_number > 64):
        raise ValueError("Not a valid square")

    return pow(2, (integer_number-1))


def total_after(integer_number):
    """ Calculates the sum of all the squares upto the given number. 
    """
    if (integer_number < 1 or integer_number > 64):
        raise ValueError("Not a valid square")

    return sum([on_square(x) for x in range(1, integer_number + 1)])
