import physicalobject
import math
import pyglet
from game import resources
import bullet
from pyglet.window import key


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.bullet_speed = 700.0
        self.key_handler = key.KeyStateHandler()
        self.reacts_to_bullets = False
        self.fire_cooldown = 0.0
        self.fire_limit = 100.0

        # need to delete the initial 'img' kwarg
        if kwargs.get('img'):
            del kwargs['img']

        self.flame_sprite = pyglet.sprite.Sprite(
            img=resources.flame_image, *args, **kwargs)
        self.flame_sprite.visible = False

    def rotate(self, dt):
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

    def check_limits(self):
        if self.velocity_x > 300:
            self.velocity_x = 300
        elif self.velocity_x < -300:
            self.velocity_x = -300

        if self.velocity_y > 300:
            self.velocity_y = 300
        elif self.velocity_y < -300:
            self.velocity_y = -300

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt

            self.velocity_x += force_x
            self.velocity_y += force_y

            self.check_limits()

            self.flame_sprite.rotation = self.rotation
            self.flame_sprite.x = self.x
            self.flame_sprite.y = self.y
            self.flame_sprite.visible = True
        else:
            self.flame_sprite.visible = False

        if self.key_handler[key.SPACE]:
            if self.fire_cooldown > 15:
                self.fire_cooldown = 0
                self.fire()
            else:
                self.fire_cooldown += self.fire_limit * dt

    # def on_key_press(self, symbol, modifiers):
        # if symbol == key.SPACE:
            # self.fire()

    def fire(self):
        angle_radians = -math.radians(self.rotation)

        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(x=bullet_x, y=bullet_y, batch=self.batch)

        bullet_vx = (self.velocity_x + math.cos(angle_radians) *
                     self.bullet_speed)
        bullet_vy = (self.velocity_y + math.sin(angle_radians) *
                     self.bullet_speed)

        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy

        self.new_objects.append(new_bullet)

    def delete(self):
        self.flame_sprite.delete()
        super(Player, self).delete()
