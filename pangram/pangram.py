#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20181205
@author: chelwin
"""
#import only the bare essentials so that you don't 
#inadvertantly mix up the local variables.
from string import ascii_lowercase
def is_pangram(sentence):
    alpha = set(ascii_lowercase)
#use the method of class set to check if a set is the
#subset of a string. Now the logic is beyond me.
    return alpha.issubset(sentence.lower())


s = is_pangram("abc def ghi jlk mon prq stu vxw zy.")
print(s)
