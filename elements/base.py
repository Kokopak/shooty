#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
from math import atan2, cos, sin

import element
import config


class Base(element.Element):
    
    def __init__(self, img, x=0, y=0):
        super(Base, self).__init__(img=img)

        self.scale_properly()
        self.x = config.WIDTH / 2
        self.y = self.height
