import random

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
	def rando_lyric(self):
		return self.lyrics[random.randint(0, len(self.lyrics) - 1)]

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

while True:
	print happy_bday.rando_lyric()
	raw_input('CTRL-C to make it stahp > ')