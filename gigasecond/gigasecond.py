#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

def add_gigasecond(birth_date):
    """Returns time when the birth_date completes 1 million(giga) seconds.
   
    Keyword arguments;
    birth_date -- an object of class datetime
    
    Considering the leap years as distinct from the average years,
    include the method for distinguishing and calculating the number of 
    leap years in a given birth_date's lifetime.
    """
    return birth_date + timedelta(seconds=pow(10,9))

