import pyglet
import physicalobject
import resources
import random


class Asteroid(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(img=resources.asteroid_image,
                                       *args, **kwargs)

    def randomcoords(self, player_pos, edge):
        asteroid_x = random.randint(0, 800)
        asteroid_y = random.randint(0, 600)
        side = random.randint(1, 4)

        if side == 1:
            if edge:
                asteroid_y = 600 + (self.length / 2)
            else:
                diff = player_pos[1] + 100
                asteroid_y = random.randint(diff, 600)
        elif side == 2:
            if edge:
                asteroid_y = -self.length / 2
            else:
                diff = player_pos[1] - 100
                asteroid_y = random.randint(0, diff)
        elif side == 3:
            if edge:
                asteroid_x = -self.width / 2
            else:
                diff = player_pos[0] - 100
                asteroid_x = random.randint(0, diff)
        elif side == 4:
            if edge:
                asteroid_x = 800 + (self.width / 2)
            else:
                diff = player_pos[0] + 100
                asteroid_x = random.randint(diff, 800)

        return asteroid_x, asteroid_y

    def randomize(self, player_pos, x=None, y=None, edge=False):
        if player_pos:
            asteroid_x, asteroid_y = self.randomcoords(player_pos, edge)

        if x is None:
            self.x = asteroid_x
        else:
            self.x = x
        if y is None:
            self.y = asteroid_y
        else:
            self.y = y

        self.rotation = random.randint(0, 360)
        self.velocity_x = random.randint(-40, 40)
        self.velocity_y = random.randint(-40, 40)
        self.rotate_speed = random.randint(-40, 40)

    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)

        if self.dead and self.scale > 0.25:
            num_asteroids = random.randint(2, 3)
            spawn_pos = [(self.x - self.image.anchor_x, self.y),
                         (self.x + self.image.anchor_x, self.y),
                         (self.x, self.y - self.image.anchor_y),
                         (self.x, self.y + self.image.anchor_y)]

            for i in xrange(num_asteroids):
                add_to = Asteroid(batch=self.batch)
                coord = spawn_pos.pop(0)

                add_to.randomize(None, coord[0], coord[1])
                add_to.scale = self.scale * 0.5

                self.new_objects.append(add_to)
