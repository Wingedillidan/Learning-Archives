import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'NY', 'Rochester')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
print "NY State has:", hashmap.get(cities, 'NY')
print "OR State has:", hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is:", hashmap.get(states, 'Michigan')
print "Florida's abbreviation is:", hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan's abbreviation is: ", hashmap.get(cities, hashmap.get(states, 'Michigan')[0])
print "Florida's abbreviation is: ", hashmap.get(cities, hashmap.get(states, 'Florida')[0])

# print every abbreviation
print '-' * 10
hashmap.list(states)

# print every city in state
print '-' * 10
hashmap.list(cities)

print '-' * 10
# safely get a abbreviation by state that might not be there
state = hashmap.get(states, 'Texas')

assert state, "Sorry, no Texas."
	
# get a city with a default value
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city