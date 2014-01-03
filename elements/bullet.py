#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import element
import config


class Bullet(element.Element):
    
    def __init__(self, img, x=0, y=0):
        super(Bullet, self).__init__(img=img)