import pyglet
from pyglet.window import key
from game import resources
from game import load
from game.player import Player

game_window = pyglet.window.Window(800, 600, resizable=True)
UI_batch = pyglet.graphics.Batch()
main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label("Score: 0", x=10, y=575, batch=UI_batch)
level_label = pyglet.text.Label("Learning Pyglet :D",
                                x=400, y=575, anchor_x='center',
                                batch=UI_batch)

player_ship = Player(
    img=resources.player_image, x=400, y=300, batch=main_batch)
player_lives = load.player_lives(3, UI_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)

game_objects = [player_ship] + asteroids


def update(dt):
    to_add = []

    for obj in game_objects:
        obj.update(dt)

        to_add.extend(obj.new_objects)
        obj.new_objects = []

        if obj.dead:
            obj.delete()
            game_objects.remove(obj)

    game_objects.extend(to_add)

    for i in xrange(len(game_objects)):
        for j in xrange(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

if __name__ == "__main__":
    @game_window.event
    def on_draw():
        game_window.clear()

        main_batch.draw()
        UI_batch.draw()

    @game_window.event
    def on_key_press(symbol, modifier):
        if symbol == key._1:
            print "POOP"
            pyglet.app.exit()
            pyglet.clock.fps_limit = 15
            pyglet.app.run()

    game_window.push_handlers(player_ship.key_handler)
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
