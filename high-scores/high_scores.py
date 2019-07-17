#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on Friday, 5 July 2019 at 12:22:27

@author: vsanc
"""


def latest(scores):
    """ Return the score of the last game.
    """
    return scores[-1]


def personal_best(scores):
    """ Return the the high score.  
    """
#    return sorted(scores, reverse=True)[0]
    return max(scores)

def personal_top_three(scores):
    """ Return the three highest scores. 
    """
    return sorted(scores, reverse=True)[:3]
