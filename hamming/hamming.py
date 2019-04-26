#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Friday, 26 April 2019 at 14:59:03

@author: vsanc
"""
import string

def distance(strand_a, strand_b)->int: 
    space_strand = 0    
    if len(strand_a) == len(strand_b):
        for index in range(len(strand_a)):
            if strand_a[index] != strand_b[index]:
                space_strand += 1
    else: 
        raise ValueError("The identical DNA strands are not of the same length!")
    return space_strand


#strand_a = "GGCCTACTAACGGGAT"
#strand_b = "CATCGTAATGACGGCCT"
#print(strand_a + "\n" + strand_b + "\n" + str(distance(strand_a,strand_b)))

