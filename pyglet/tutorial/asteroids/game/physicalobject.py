import pyglet
from game import util


class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x = 0
        self.velocity_y = 0
        self.rotate_speed = 0
        self.dead = False
        self.new_objects = []
        self.reacts_to_bullets = True
        self.is_bullet = False

    def rotate(self, dt):
        if self.rotation > 360:
            self.rotation = 0
        elif self.rotation < 0:
            self.rotation = 360

        self.rotation += self.rotate_speed * dt

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.check_bounds()

        if self.rotate_speed:
            self.rotate(dt)

    def check_bounds(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + (self.image.width / 2)
        max_y = 600 + (self.image.height / 2)

        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x

        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def collides_with(self, other_object):
        if not self.reacts_to_bullets and other_object.is_bullet:
            return False
        if self.is_bullet and not other_object.reacts_to_bullets:
            return False

        collision_distance = ((self.image.width / 2) * self.scale) + \
            ((other_object.image.width / 2) * other_object.scale)

        actual_distance = util.distance(self.position, other_object.position)

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        if not other_object.__class__ == self.__class__:
            self.dead = True
