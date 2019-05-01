#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20190416
@author:Chelwin
"""


def two_fer(name=""):
    first = "One for "
    last = ", one for me."
 
    return first + name + last if name else first + "you" + last
