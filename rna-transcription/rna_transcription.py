#!usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Created on Sunday, 28 April 2019 at 19:32:32

@author: vsanc
"""
def to_rna(dna_strand):
    rna_list = []
    for ch in dna_strand:
        rna_list.extend('C' if ch=='G' else 'G' if ch=='C' else 'A' if ch=='T' else 'U',end=' ')
    return rna_list
 



###### TEST SUITE #######
dna_strand = 'GGTA'
print(to_rna(dna_strand))
