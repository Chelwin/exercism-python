#!usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
Created on Sunday, 28 April 2019 at 19:32:32

@author: vsanc
"""


def to_rna(dna_strand):

    nucleotides = set('GCTA')
    if set(dna_strand).difference(nucleotides):
        raise ValueError("The DNA strand has foreign nucleotide/s!")

    replace_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    return ''.join(list(map(lambda x: replace_dict[x], dna_strand)))
