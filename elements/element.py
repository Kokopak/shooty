#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import math
from pyglet.gl import gl

class Element(pyglet.sprite.Sprite):

    def __init__(self, img, x, y, scale):
        pyglet.sprite.Sprite.__init__(self, img=img, x=x, y=y)

        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2

        self.velocity_x = 0.0
        self.velocity_y = 0.0

        self.scale_factor = scale
        self.scale_properly()

    def scale_properly(self) :
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        self.scale = self.scale_factor

    def collide_with(self, other):
        distance = math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        return distance <= other.height
