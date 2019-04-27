#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Friday, 26 April 2019 at 14:59:03

@author: vsanc
"""

def distance(strand_a,strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Both strands must be of the same length.")
    else:
        DNATuple = list(zip(strand_a, strand_b))
        return sum([1 for elem in DNATuple if elem[0]!=elem[1]])




######## TEST SUITE #########

#Raises a ValueError and exits process
strand_a = "AGTACTATA"
strand_b = "ACTAGTATAA"
print(strand_a + "\n" + strand_b + "\n" + str(distance(strand_a,strand_b)))

#Prints the number of differences
strand_a = "AGTACTATA"
strand_b = "ACTAGTATA"
print(strand_a + "\n" + strand_b + "\n" + str(distance(strand_a,strand_b)))

