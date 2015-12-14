from nose.tools import *
from ex48 import parser
from ex48 import lexicon


def test_peek():
    sentence = lexicon.scan("eat all the things")
    assert_equal(parser.peek(sentence), "verb")
    assert_equal(parser.peek([]), None)


def test_match():
    # test successful returning case
    sentence = [('verb', 'go')]
    assert_equal(parser.match(sentence, 'verb'), ('verb', 'go'))

    # test with an incorrect expected case
    sentence = lexicon.scan("north and beyond the wall")
    assert_equal(parser.match(sentence, 'noun'), None)

    # test with passing an empty list
    assert_equal(parser.match([], 'direction'), None)


def test_skip():
    # test a standard use case
    sentence = lexicon.scan("the the in of go the")
    parser.skip(sentence, 'stop')
    assert_equal(sentence, [('verb', 'go'), ('stop', 'the')])

    # a case where nothing should happen
    sentence = lexicon.scan("the the in of go the")
    result = lexicon.scan("the the in of go the")
    parser.skip(sentence, 'verb')
    assert_equal(sentence, result)


def test_parse_verb():
    sentence = lexicon.scan("go")
    assert_equal(parser.parse_verb(sentence), ('verb', 'go'))

    sentence = lexicon.scan("the in eat")
    assert_equal(parser.parse_verb(sentence), ('verb', 'eat'))

    sentence = lexicon.scan("cheese")
    with assert_raises(parser.ParserError):
        parser.parse_verb(sentence)


def test_parse_subject():
    sentence = lexicon.scan("bear")
    assert_equal(parser.parse_subject(sentence), ('noun', 'bear'))

    sentence = lexicon.scan("in in from the go")
    assert_equal(parser.parse_subject(sentence), ('noun', 'player'))

    with assert_raises(parser.ParserError):
        sentence = lexicon.scan("oh poop")
        parser.parse_subject(sentence)


def test_parse_object():
    sentence = lexicon.scan("door")
    assert_equal(parser.parse_object(sentence), ('noun', 'door'))

    sentence = lexicon.scan("in the bear")
    assert_equal(parser.parse_object(sentence), ('noun', 'bear'))

    sentence = lexicon.scan("in the the north bear")
    assert_equal(parser.parse_object(sentence), ('direction', 'north'))

    sentence = lexicon.scan("for the go bear")
    with assert_raises(parser.ParserError):
        parser.parse_object(sentence)


def test_parse_sentence():
    sentence = lexicon.scan("go in the door")
    sentence = parser.parse_sentence(sentence)
    result = parser.Sentence(('noun', 'player'),
                             ('verb', 'go'),
                             ('noun', 'door'))
    assert_equal(sentence.subject, result.subject)
    assert_equal(sentence.verb, result.verb)
    assert_equal(sentence.obj, result.obj)

    with assert_raises(parser.ParserError):
        sentence = lexicon.scan("go eat the player")
        parser.parse_sentence(sentence)
