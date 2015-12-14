import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()


"""@window.event
def on_key_press(symbol, modifiers):
    print 'A key was pressed :O'
    print symbol, modifiers

    if symbol == key.A:
        print 'a'


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print "CLICK'D"""

window.push_handlers(pyglet.window.event.WindowEventLogger())


@window.event
def on_draw():
    window.clear()

pyglet.app.run()
