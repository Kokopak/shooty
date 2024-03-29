#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pyglet
import config
import random

from elements import *


class Game(pyglet.window.Window):

    def __init__(self):

        pyglet.window.Window.__init__(self)
        self.set_size(config.WIDTH, config.HEIGHT)
        self.set_caption("Shooty")

        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.b = base.Base(img=config.IMG_BASE, x=config.WIDTH/2, y=(config.IMG_BASE.height * config.SCALE)/2, scale=config.SCALE)
        self.g = gun.Gun(img=config.IMG_GUN, x=self.b.x, y=self.b.y + self.b.height/8, scale=config.SCALE)
        #self.g.enable_power_shoot()

        for handl in self.g.event_handlers:
            self.push_handlers(handl)

        self.enemies = []
        self.enemies_kills = 0
        self.spawn_enemies = True
        self.spawn_boss = False
        self.boss = enemy.Enemy(img=config.IMG_ENEMY,
            x=config.WIDTH / 2,
            y=config.HEIGHT - config.IMG_ENEMY.height * config.SCALE * 2,
            scale=config.SCALE * 2,
            life=10,
            boss=True)

        self.fps_display = pyglet.clock.ClockDisplay()

    def update(self, dt):
        self.g.update(dt)
        for bullet in self.g.bullets:
            if bullet.out_of_screen():
                self.g.bullets.remove(bullet)
                bullet.set_died(True)
            for e in self.enemies:
                if bullet.collide_with(e) :
                    e.life -= 1
                    if e.life <= 0:
                        if e.boss:
                            self.spawn_boss = False
                        self.enemies.remove(e)
                        self.enemies_kills += 1
                    if bullet.died == False:
                        self.g.bullets.remove(bullet)
            bullet.update(dt)

        for e in self.enemies:
            e.update(dt)
            if e.collide_with(self.b):
                e.x -= self.b.width * dt
            if e.out_of_screen():
                #On perd des PV
                self.enemies.remove(e)


        if self.enemies_kills == 5:
            self.spawn_boss = True

        if self.spawn_boss:
            self.enemies = []
            self.spawn_enemies = False
            self.enemies.append(self.boss)

    def on_draw(self):
        self.clear()
        self.b.draw()
        self.g.draw()
        self.fps_display.draw()
        for bullet in self.g.bullets:
            bullet.draw()

        for e in self.enemies:
            e.draw()



    def add_enemy(self, dt):
        if self.spawn_enemies :
            x = random.randint(config.IMG_ENEMY.width * config.SCALE, config.WIDTH - config.IMG_ENEMY.width * config.SCALE)
            y = config.HEIGHT + config.IMG_ENEMY.height * config.SCALE
            e = enemy.Enemy(img=config.IMG_ENEMY,
                x=x,
                y=y,
                scale=config.SCALE,
                life=1)
            self.enemies.append(e)


if __name__ == "__main__":
    game = Game()
    pyglet.clock.schedule_interval(game.update, 1/60.0)
    # Ajout un ennemi toutes les 2 sec
    pyglet.clock.schedule_interval(game.add_enemy, 2)
    pyglet.app.run()
