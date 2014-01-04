#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import math
import bullet as bu
import element
import config


from pyglet.window import key


class Gun(element.Element):

    def __init__(self, img, x, y, scale):
        element.Element.__init__(self, img=img, x=x, y=y, scale=scale)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.rotate_speed = 200.0
        self.bullets = []
        self.rotation = 180
        
    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt

        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def fire(self):
        angle_radians = -math.radians(self.rotation) - math.pi / 2
        gun_radius = self.height

        bullet = bu.Bullet(img=pyglet.image.load("img/bullet.png"), 
            x=self.x + math.cos(angle_radians) * gun_radius,
            y=self.y + math.sin(angle_radians) * gun_radius,
            scale=1)
        bullet.calc_velocity(angle_radians)
        bullet.rotation = self.rotation

        self.bullets.append(bullet)
