#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
from datetime import datetime

def add_gigasecond(birth_date):
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
