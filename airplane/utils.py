def trim(answer, options):
    remove = []

    for char in answer:
        for i in xrange(len(options)-1):
            if char not in options[i]:
                remove.append(i)

        for item in remove:
            del options[item]

        remove = []


def parse_answer(answer, options):
    """Parses the player's answer based on matching characters"""

    result = []

    if type(options) == dict:
        for key in options:
            result.append(key)
    elif type(options) == list:
        for item in options:
            result.append(item)
    else:
        raise TypeError

    return trim(answer, result)

if __name__ == '__main__':
    options = {'pie': 1, 'cake': 2, 'poop': 3,
               'waffles': 4, 'pancakes': 5,
               'apple': 6, 'cheese': 7}
    answer = raw_input('> ')

    print parse_answer(answer, options)
    print options
