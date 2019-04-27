#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
from datetime import datetime

def eins_add_gigasecond(birth_date):
    giga_float_years = pow(10,9)/(60*60*24*365)
    birth_date_float_years = birth_date.year+(birth_date.month/12)
    +(birth_date.day/30)+(birth_date.hour/24)
    +(birth_date.minute/60)+(birth_date.second/60)
    years = giga_float_years + birth_date_float_years
    years_copy = years
    years = floor(years_copy)
    months = (years_copy%years)*12
    months_copy = months
    months = floor(months_copy)
    days = (months_copy%months)*30
    days_copy = days
    days = floor(days_copy)
    hours = (days_copy%days)*24
    hours_copy = hours
    hours = floor(hours_copy)
    minutes = (hours_copy%hours)*60
    minutes_copy = minutes 
    minutes = floor(minutes_copy)
    seconds = (minutes_copy%minutes)*60
    seconds_copy = seconds
    seconds = floor(seconds_copy)
    
    
    return datetime(years,months,days,hours,minutes,seconds)

def is_leap_year()

def zwei_add_gigasecond(birth_date):
    """Returns time when the birth_date completes 10 billion seconds.
   
    Keyword arguments;
    birth_date -- an object of class datetime
    
    Considering the leap years as distinct from the average years,
    include the method for distinguishing an calculating the number of 
    leap years in a given birth_date's lifetime.
    """    
