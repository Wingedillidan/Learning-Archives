def wrapper(func):
    def shout(sentence, letter):
        sentence = sentence.upper()
        letter = letter.upper()

        return func(sentence, letter)

    return shout


@wrapper
def removeletter(sentence, letter):
    return sentence.replace(letter, '')

if __name__ == "__main__":
    sentence = raw_input('enter a sentence > ')
    letter = raw_input('take away which letter > ')

    print removeletter(sentence, letter)
