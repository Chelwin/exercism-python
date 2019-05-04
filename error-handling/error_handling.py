#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday, 1 May 2019 at 18:30:38

@author: vsanc
"""


def handle_error_by_throwing_exception():
    raise Exception("ERROR!")


def handle_error_by_returning_none(input_data):
    
    try:
        return int(input_data) if isinstance(int(input_data),int) else None
    except ValueError:
        print('Invalid input!')

def handle_error_by_returning_tuple(input_data):
    pass


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        open(filelike_object,'r')
    except:
        raise IOError("File not available!")
    finally:
        filelike_object.close()
