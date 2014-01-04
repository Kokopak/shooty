#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import config

from elements import *

window = pyglet.window.Window(width=config.WIDTH, height=config.HEIGHT, caption="Shooty")
pyglet.gl.glClearColor(1, 1, 1, 1)

b = base.Base(img=config.IMG_BASE, x=config.WIDTH/2, y=config.IMG_BASE.height * 8, scale=8)
g = gun.Gun(img=config.IMG_GUN, x=b.x, y=b.height/8, scale=8)

for handl in g.event_handlers:
    window.push_handlers(handl)

fps_display = pyglet.clock.ClockDisplay()

def update(dt):
    g.update(dt)
    for bullet in g.bullets:
        bullet.update(dt)
        if bullet.out_of_screen():
            g.bullets.remove(bullet)

@window.event
def on_draw():
    window.clear()
    b.draw()
    g.draw()
    fps_display.draw()
    for bullet in g.bullets:
        bullet.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
