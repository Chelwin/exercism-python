#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on Friday, 5 July 2019 at 12:52:05 

@author: vsanc
"""


def prime_factors(natural_number) -> list:
    """ Find the prime factors of the number.
    """
    if (natural_number < 1):
        raise ValueError("Not a natural number.")

# Incomplete algorithm -- mine in the notebook has a bug.
# It ignores the multiple occurances of one prime factor. 
# The algorithm needs to ackowledge these occurances.
# Probably can be solved by a loop that increments p only 
# after the number-mod-p is no more zero.
    p = 2
    if !(natural_number**2 >= p**2 ):
        return [natural_number]
    else:
       if !(mod(natural_number, p) == 0):
           p = p + 1 
           prime_factors(nat)
