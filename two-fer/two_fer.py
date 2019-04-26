#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20190416
@author:Chelwin
"""

def two_fer(name=""):
    statement = "One for "
    if name:
        statement = statement + name
    else:
        statement = statement + "you"
    conclusion = ", one for me."

    return statement + conclusion

#print(two_fer("sierra"))
#print(two_fer())
#print(two_fer("alpha romeo"))

