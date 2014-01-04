#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import pyglet
from pyglet.window import key, mouse

import elements

import config


window = pyglet.window.Window(width=config.WIDTH, height=config.HEIGHT, caption="Shooty")
pyglet.gl.glClearColor(1, 1, 1, 1)


base = elements.base.Base(img=pyglet.image.load("img/base.png"), x=config.WIDTH/2, y=0, scale=8)
base.y = base.height

gun = elements.gun.Gun(img=pyglet.image.load("img/gun.png"), x=base.x, y=0, scale=8)
for handl in gun.event_handlers:
    window.push_handlers(handl)
gun.y = base.height / 8

fps_display = pyglet.clock.ClockDisplay()


def update(dt):
    gun.update(dt)
    print gun.bullets
    for bullet in gun.bullets:
        bullet.update(dt)
        if bullet.out_of_screen():
            gun.bullets.remove(bullet)

@window.event
def on_draw():
    window.clear()
    base.draw()
    gun.draw()
    fps_display.draw()
    for bullet in gun.bullets:
        bullet.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
