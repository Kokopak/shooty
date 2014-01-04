#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import config
import random

from elements import *

window = pyglet.window.Window(width=config.WIDTH, height=config.HEIGHT, caption="Shooty")
pyglet.gl.glClearColor(1, 1, 1, 1)

b = base.Base(img=config.IMG_BASE, x=config.WIDTH/2, y=(config.IMG_BASE.height * config.SCALE)/2, scale=config.SCALE)
g = gun.Gun(img=config.IMG_GUN, x=b.x, y=b.y + b.height/8, scale=config.SCALE)
g.enable_power_shoot()

for handl in g.event_handlers:
    window.push_handlers(handl)

enemies = []

fps_display = pyglet.clock.ClockDisplay()

def update(dt):
    g.update(dt)
    for bullet in g.bullets:
        if bullet.out_of_screen():
            g.bullets.remove(bullet)
            bullet.set_died(True)
        for e in enemies:
            if bullet.collide_with(e) :
                enemies.remove(e)
                if bullet.died == False:
                    g.bullets.remove(bullet)
        bullet.update(dt)

    for e in enemies:
        e.update(dt)
        if e.out_of_screen():
            enemies.remove(e)

@window.event
def on_draw():
    window.clear()
    b.draw()
    g.draw()
    fps_display.draw()
    for bullet in g.bullets:
        bullet.draw()

    for e in enemies:
        e.draw()


def add_enemy(dt):
    x = random.randint(config.IMG_ENEMY.width * config.SCALE, config.WIDTH - config.IMG_ENEMY.width * config.SCALE)
    y = config.HEIGHT + config.IMG_ENEMY.height * config.SCALE
    e = enemy.Enemy(img=config.IMG_ENEMY,
        x=x,
        y=y,
        scale=config.SCALE)
    enemies.append(e)

pyglet.clock.schedule_interval(update, 1/60.0)
# Ajout un ennemi toutes les 2 sec
pyglet.clock.schedule_interval(add_enemy, 2)
pyglet.app.run()
