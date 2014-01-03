#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import gl

class Element(pyglet.sprite.Sprite):
    
    def __init__(self, img, x=0, y=0):
        pyglet.sprite.Sprite.__init__(self, img=img, x=x, y=y)

        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height

        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def scale_properly(self) :
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        self.scale = 8