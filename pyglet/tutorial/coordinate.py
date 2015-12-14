class Coordinate(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Coordinate(x={x}, y={y})'.format(x=self.x, y=self.y)


def coordcontrol(func):
    def inner(a, b):
        for coord in [a, b]:
            if coord.x < 0:
                coord.x = 0
            if coord.y < 0:
                coord.y = 0

        result = func(a, b)

        if result.x < 0:
            result.x = 0
        if result.y < 0:
            result.y = 0

        return result

    return inner


@coordcontrol
def add(a, b):
    x = a.x + b.x
    y = a.y + b.y

    return Coordinate(x, y)


@coordcontrol
def sub(a, b):
    x = a.x - b.x
    y = a.y - b.y

    return Coordinate(x, y)

if __name__ == "__main__":
    coords = [0] * 2
    print coords

    while True:
        coords = [0] * 2

        for i in xrange(2):
            x = raw_input('x' + str(i+1) + ' > ')
            y = raw_input('y' + str(i+1) + ' > ')

            try:
                coords[i] = Coordinate(int(x), int(y))
            except ValueError:
                break

        try:
            print add(coords[0], coords[1])
        except AttributeError:
            print "Invalid input(s), integers only!"
