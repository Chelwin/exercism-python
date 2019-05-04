#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Created on Friday, 3 May 2019 at 17:05:55

@author: vsanc
"""


import string
import random


class Robot(object):
    NAMELIST = []

    def __init__(self):
        """ Assign a name to the robot and remember it's name.
        """
        self.FIRSTNAME = list(string.ascii_uppercase)
        self.LASTNAME = list(string.digits)
        self.name = None

        self.getRobotName()

    def getRobotName(self):
        """ Assign a name to the robot
        """
        first = ''.join(random.choices(self.FIRSTNAME, k=2))
        last = ''.join(random.choices(self.LASTNAME, k=3))
        name = first + last
        if name not in self.NAMELIST:
            self.name = name
            self.NAMELIST.append(self.name)
        else:
            self.getRobotName()

    def reset(self):
        """ Reset the Robot to default factory settings.
        """
        self.getRobotName()
