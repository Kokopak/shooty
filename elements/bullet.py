#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import element
import config
import math


class Bullet(element.Element):
    
    def __init__(self, img, x, y, scale):
        element.Element.__init__(self, img=img, x=x, y=y, scale=scale)
        self.speed = 500

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        if self.out_of_screen() :
            del self

    def out_of_screen(self):
        return self.x < 0 or self.y < 0 or self.x > config.WIDTH or self.y > config.HEIGHT

    def calc_velocity(self, angle_radians) :
        self.velocity_x = self.velocity_x + math.cos(angle_radians) * self.speed
        self.velocity_y = self.velocity_y + math.sin(angle_radians) * self.speed