import pyglet
import random
import resources
import physicalobject
import util
import asteroid


no_spawn_regions = []


def binarysearch(num, li):
    mid = (len(li) / 2) - 1

    if mid <= 1:
        return mid
    if num == li[mid]:
        return mid

    if num < li[mid]:
        return binarysearch(num, li[:mid])
    elif num > li[mid]:
        return binarysearch(num, li[mid:])


def asteroids(num_asteroids, player_pos, batch=None):
    asteroids = [0] * num_asteroids

    for i in xrange(num_asteroids):
        asteroids[i] = asteroid.Asteroid(batch=batch)
        asteroids[i].randomize(player_pos)

    return asteroids


def player_lives(num_icons, batch=None):
    player_lives = []

    for i in xrange(num_icons):
        new_sprite = pyglet.sprite.Sprite(
            img=resources.player_image, x=785-i*30, y=585,
            batch=batch)

        new_sprite.scale = 0.5
        player_lives.append(new_sprite)

    return player_lives
