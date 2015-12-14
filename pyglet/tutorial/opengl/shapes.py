import pyglet
from pyglet.gl import *

screen = pyglet.window.Window(800, 600)

COLOR_CHANGE_RATE = 0


def _colormixer(color, color_meta):
    shift = False

    for i in xrange(len(color)):
        if color_meta[i] == 'down':
            color[i] -= COLOR_CHANGE_RATE

            if color[i] <= 0:
                color[i] = 0
                shift = True
        elif color_meta[i] == 'up':
            color[i] += COLOR_CHANGE_RATE

            if color[i] >= 255:
                color[i] = 255
                shift = True

    if shift:
        temp = [None] * 4
        for i in xrange(len(color_meta)):
            if color_meta[i]:
                temp[i+1] = color_meta[i]

        temp[0] = temp.pop(3)
        color_meta = temp

    return color, color_meta


def colormagizer(color, color_meta):
    if type(color[0]) is list:
        for i in xrange(len(color)):
            color[i], color_meta[i] = _colormixer(color[i], color_meta[i])
    else:
        color, color_meta = _colormixer(color, color_meta)

color1 = [255.0, 0.0, 0.0]
color1_meta = ['down', 'up', None]
color2 = [0.0, 255.0, 0.0]
color2_meta = [None, 'down', 'up']
color3 = [0.0, 0.0, 255.0]
color3_meta = ['up', None, 'down']


def update(dt):
    colormagizer([color1, color2, color3],
                 [color1_meta, color2_meta, color3_meta])


@screen.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glBegin(GL_TRIANGLES)
    glColor3f(color1[0], color1[1], color1[2])
    glVertex2f(screen.width/2, screen.height)
    glColor3f(color2[0], color2[1], color2[2])
    glVertex2f(0, 0)
    glColor3f(color3[0], color3[1], color3[2])
    glVertex2f(screen.width, 0)
    glEnd()

    screen.flip()


@screen.event
def on_key_press(symbol, modifier):
    if symbol == pyglet.window.key.SPACE:
        print "POOP"

pyglet.app.run()
