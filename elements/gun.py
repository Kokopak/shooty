#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import math
import bullet as bu
import element
import config


from pyglet.window import key


class Gun(element.Element):

    def __init__(self, img, x=0, y=0):
        super(Gun, self).__init__(img=img)

        self.scale_properly()

        self.key_handler = key.KeyStateHandler()

        self.event_handlers = [self, self.key_handler]

        self.rotate_speed = 200.0

        self.bullet_speed = 500
        self.bullets = []

        self.image.anchor_x = self.image.width/2
        self.image.anchor_y = self.image.height

        self.rotation = 180
        self.x = config.WIDTH / 2
        self.y = self.height / 4


    def update(self, dt):
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt

        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        for bullet in self.bullets:
            bullet.x += bullet.velocity_x * dt
            bullet.y += bullet.velocity_y * dt

            if bullet.x < 0 or bullet.y < 0 or bullet.x > config.WIDTH or bullet.y > config.HEIGHT:
                self.bullets.remove(bullet)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def fire(self):
        angle_radians = -math.radians(self.rotation) - math.pi / 2
        gun_radius = self.height

        bullet = bu.Bullet(img=pyglet.image.load("img/bullet.png"))
    
        bullet.x = self.x + math.cos(angle_radians) * gun_radius
        bullet.y = self.y + math.sin(angle_radians) * gun_radius

        bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
        bullet_vy = self.velocity_y + math.sin(angle_radians) * self.bullet_speed

        bullet.velocity_x = bullet_vx
        bullet.velocity_y = bullet_vy

        self.bullets.append(bullet)
