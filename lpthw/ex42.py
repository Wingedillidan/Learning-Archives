## animal is-a object
class animal(object):

	def myname(self):
		if hasattr(self, 'name'):
			if hasattr(self, 'talk'):
				self.salutation = "%s, my name is, %s!" % (self.talk.capitalize(), self.name)
			else:
				self.salutation = "My name is, %s!", self.name
		else:
			self.salutation = "I have no name :c"

## dog is-a animal
class dog(animal):
	
	def __init__(self, name):
		## dog has-a name
		self.name = name
		self.talk = "woof"
	
	# def myname(self):
		# print "My name is,", self.name

## cat is-a animal
class cat(animal):
	
	def __init__(self, name):
		## cat has-a name
		self.name = name
		self.talk = "meow"

## person is-a object
class person(object):
	
	def __init__(self, name):
		## person has-a name
		self.name = name
		
		## person has-a pet of some kind
		self.pet = None

## employee is-a person
class Employee(person):

	def __init__(self, name, salary):
		## employee has-a name
		super(Employee, self).__init__(name)
		## employee has-a salary
		self.salary = salary

## fish is-a object
class fish(object):
	pass

## salmon is-a fish
class salmon(fish):
	pass

## halibut is-a fish
class halibut(fish):
	pass

## rover is-a dog
rover = dog("Rover")

## satan is-a cat
satan = cat("Satan")

## mary is-a person
mary = person("Mary")

## mary has-a pet (named Satan)
mary.pet = satan
mary.pet.myname()
print mary.pet.salutation

## frank is a employee who has-a salary (of 120000)
frank = Employee("Frank", 120000)

## frank has-a pet (named Rover)
frank.pet = rover

## flipper is-a fish
flipper = fish()

## crouse is-a salmon
crouse = salmon()

## harry is-a halibut
harry = halibut()

rando = animal()
rando.myname()