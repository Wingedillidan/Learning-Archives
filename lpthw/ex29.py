people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"


dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
elif people <= dogs:
	print "Cow."

if people <= dogs:
	print "People are less than or equal to dogs."
else:
	print "Moo."

if dogs + 1 < cats - 5:
	print "Cats win hard D="

if people == dogs:
	print "People are dogs."