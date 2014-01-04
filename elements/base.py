#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
from math import atan2, cos, sin

import element
import config


class Base(element.Element):
    
    def __init__(self, img, x, y, scale):
        element.Element.__init__(self, img=img, x=x, y=y, scale=scale)