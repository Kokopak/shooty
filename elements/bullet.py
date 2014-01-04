#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import element
import config
import math

class Bullet(element.Element):

    def __init__(self, img, x, y, scale, angle, rotation):
        element.Element.__init__(self, img=img, x=x, y=y, scale=scale)
        self.speed = 150
        self.velocity_x = math.cos(angle) * self.speed
        self.velocity_y = math.sin(angle) * self.speed
        self.rotation = rotation
        self.died = False

    def set_died(self, died):
        self.died = died

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def out_of_screen(self):
        return self.x < 0 or self.y < 0 or self.x > config.WIDTH or self.y > config.HEIGHT

    def collide_with(self, enemy):
        distance = math.sqrt((self.x-enemy.x)**2 + (self.y-enemy.y)**2)
        return distance <= enemy.height
