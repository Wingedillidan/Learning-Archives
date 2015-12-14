class EmptyObjectException(Exception):

    def __init__(self):
        pass


class BlankRoom(object):
    """The base class for all rooms within which the player will travel
    through"""

    def __init__(self, scenario, options, spacing=3, rando=False):
        """When the player enters the room, they will be prompted with the
        scenario attribute, followed by the available options. Options is a
        dictionary attribute with its keys being the actions and values
        containing the consequences"""

        self.scenario = scenario
        self.options = options
        self.spacing = spacing + 1

    def enter(self):
        print self.scenario + ('\n' * self.spacing)

    def
