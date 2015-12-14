# allowed words
directions = ("north", "south", "east", "west",
              "down", "up", "left", "right", "back")
verbs = ("go", "stop", "kill", "eat")
stops = ("the", "in", "of", "from", "at", "it")
nouns = ("door", "bear", "princess", "cabinet")


def scan(sentence):
    """Take in an input sentence, turn it into a list of words loop through
    the list of words and match each one to a type used within the lexicon."""

    # split the sentence
    words = sentence.lower().split()
    result = []

    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        else:
            try:
                result.append(('number', int(word)))
            except ValueError:
                result.append(('error', word))

    return result
