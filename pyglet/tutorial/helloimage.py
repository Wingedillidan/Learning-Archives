import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('button_disabled-52x60.bmp')


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
