import pyglet
from pyglet.gl import *

screen = pyglet.window.Window()


@screen.event
def on_draw():
    # glClear(GL_COLOR_BUFFER_BIT)
    # glLoadIdentity()
    screen.clear()

    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(screen.width, 0)
    glVertex2f(screen.width, screen.height)
    glEnd()

    print screen.width, ',', screen.height

pyglet.app.run()
