#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20181205
@author: vsanc
"""
import string
def is_pangram(sentence):
    print(sentence)
    isPangram = False
    lowercase = ""
    for ch in sentence:
        if ch.isalpha():
            if str.lower(ch) not in lowercase:
                lowercase += str.lower(ch)

    if len(string.ascii_lowercase) == len(lowercase):
        isPangram = True
    print(lowercase)
    return isPangram 
