#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pyglet
import math
import bullet
import element
import config

from pyglet.window import key

class Gun(element.Element):

    def __init__(self, img, x, y, scale):
        element.Element.__init__(self, img=img, x=x, y=y, scale=scale)

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        self.rotate_speed = 50.0
        self.bullets = []
        self.rotation = 180

        self.power_shoot_enabled = False
        self.power_shoot = False
        self.nb_tour = 0

    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt

        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt


        if self.power_shoot_enabled:
            if self.key_handler[key.X]:
                self.power_shoot = True
            else:
                self.power_shoot = False

            if self.power_shoot :
                self.rotation += 600 * dt
                self.fire()

    def enable_power_shoot(self):
        self.power_shoot_enabled = True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def fire(self):
        angle = -math.radians(self.rotation) - math.pi / 2
        gun_radius = self.height

        b = bullet.Bullet(img=config.IMG_BULLET,
            x=self.x + math.cos(angle) * gun_radius,
            y=self.y + math.sin(angle) * gun_radius,
            angle=angle,
            rotation=self.rotation,
            scale=1)
        self.bullets.append(b)
