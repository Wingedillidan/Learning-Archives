from sys import exit
import random

class Scene(object):
	
	def enter(self):
		pass
		

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		next = self.scene_map.opening_scene().enter()
		
		while True:
			next = self.scene_map.next_scene(next).enter()

class Death(Scene):
	
	comment = ['Wow, you suck...',
		'Hah, death, you deserved it...',
		'Get rekt, nubcake.',
		'Gothons win!',
		'da end, was it worth?'
	]
	
	def enter(self):
		print self.comment[random.randint(0, len(self.comment) - 1)], '\n\n\n'
		exit(0)

class CentralCorridor(Scene):

	def enter(self):
		print "A dimly lit metal passageway stretches down into darkness, along side it are    "
		print "generic vents and panels with lots of blinking lights. A figure steps out of the"
		print "darkness and reveals itself to be a Gothon! It quickly readies a firearm..."
		fails = 0
		
		while True:
			response = raw_input('> ').lower().strip()
			
			if response == 'tell joke':
				print "You only know a little bit of the Gothon tongue after attending a comedy in   "
				print "all languages class, so you tell the only joke you can muster at gunpoint:\n  "
				print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.\n"
				print "The Gothon tries desparately to hide a chuckle, yet it soon bursts into lols. "
				print "... ... ... it's as if he is paralyzed by laughter, you quickly dart into the "
				print "nearest passage without making it obvious which way you went.\n"
				
				raw_input('PRESS ENTER TO CONTINUE')
				
				return 'laserweaponarmory'
				
			elif response == 'shoot':
				print "You draw your weapon as quickly as you can, unfortunately the Gothon noticed  "
				print "your hostile intentions and quickly took aim. There's a laser sized hole in   "
				print "your noggin... HOORAY!!!! DEATH!\n"
				
				return 'death'
			
			elif fails == 3:
				print "Your hesitance is seen as a weakness to the Gothon! It chuckles for a while   "
				print "until finally deciding to shoot... HOORAY!!!! DEATH!\n"
				
				return 'death'
				
			else:
				print "Action not recognized...\n"
				print "The Gothon grunts while keeping two eyes pinned on your movements, you need to"
				print "act, and act now!"
				
				fails += 1
	
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container.  There's a keypad lock on the box"
		print "and you need the code to get the bomb out.  If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb.  The code is 3 digits."
		
		code = '%d%d%d' % (random.randint(1,9), random.randint(1,9), random.randint(1,9))
		
		for attempts in xrange(0, 10):
			guess = raw_input('> ').strip().lower()
			
			if guess == code:
				print "The container clicks open and the seal breaks, letting gas out."
				print "You grab the neutron bomb and run as fast as you can, passed the"
				print "laughter-paralysed Gothon, to the bridge where you must place it"
				print "in the right spot.\n"
				
				raw_input('PRESS ENTER TO CONTINUE')
				
				return 'bridge'
			elif guess == 'corgi':
				print "Recognized password 'corgi', overriding code:", code
				
				raw_input('PRESS ENTER TO CONTINUE')
				
				return 'bridge'
			else:
				print "BZZZZEDDD!"
				
		print "The lock buzzes one last time and then you hear a sickening"
		print "melting sound as the mechanism is fused together."
		print "You decide to sit there, and finally the Gothons blow up the"
		print "ship from their ship and you die.\n"
		return 'death'

class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the netron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship.  Each of them has an even uglier"
		print "clown costume than the last.  They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		
		action = raw_input('> ').lower().strip()
		
		if action == "throw bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			
			return 'death'
		
		elif action == "use blaster on bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can.\n"
			
			raw_input('PRESS ENTER TO CONTINUE')
			
			return 'escapepod'
		else:
			print "DOES NOT COMPUTE!"
			
			return 'bridge'
	
class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes.  It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print "but you don't have time to look.  There's 5 pods, which one"
		print "do you take?"
		
		fails = 0
		good_pod = str(random.randint(1,5))
		
		while True:
			guess = raw_input('[pod #]> ').strip()
		
			if fails == 3:
				print "You take to long deciding and the ship, the one you're on,"
				print "explodes, which means u ded.\n"
				
				return 'death'
			elif guess == good_pod or guess == 'corgi':
				print "You jump into pod %s and hit the eject button." % good_pod
				print "The pod easily slides out into space heading to"
				print "the planet below.  As it flies to the planet, you look"
				print "back and see your ship implode then explode like a"
				print "bright star, taking out the Gothon ship at the same"
				print "time.  You won!\n"
				
				raw_input('PRESS ENTER TO CONTINUE')
				
				return 'finale'
			
			elif guess in str(range(1,6)):
				print "You tried to open the door to pod %s, but it won't budge!" % guess
				print "An indicator reads that the pod is either malfunctioning or"
				print "already jettisoned"
				
				fails += 1
				
			else:
				print "You need to take action lest you go kaboom!"
				
				fails += 1

class Finale(Scene):

	def enter(self):
		print "You successfully managed to get to the surface of the foreign planet... yay!!!"
		print "You win?"
		
		exit(0)

class Map(object):
	
	scenes = {'death': Death(),
		'centralcorridor': CentralCorridor(),
		'laserweaponarmory': LaserWeaponArmory(),
		'bridge': TheBridge(),
		'escapepod': EscapePod(),
		'finale': Finale()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		return self.scenes.get(scene_name)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('centralcorridor')
a_game = Engine(a_map)
a_game.play()