#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import element
import config
import math

class Enemy(element.Element):

    def __init__(self, img, x, y, scale, life, boss=False):
        element.Element.__init__(self, img=img, x=x, y=y, scale=scale)
        self.boss = boss
        self.life = life
        if self.boss:
            self.speed = 50
        else:
            self.speed = 100

    def update(self, dt):
        self.y -= self.speed * dt
        #self.y = 550

    def out_of_screen(self):
        return self.x < 0 or self.y < 0 or self.x > config.WIDTH or self.y > config.HEIGHT + self.height
