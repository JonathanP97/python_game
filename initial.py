import inspect 

class Fighter:
	name = "Bob"
	health = 40
	strength = 10
	defense = 4
	agility = 5
	wisdom = 1.1
	
	def __setName__(self, n):
		self.name = n

	def __levelUp__(self):
		self.health += 2 * self.wisdom
		self.strength += 3 * self.wisdom
		self.defense =+ 3 * self.wisdom

	def __showStats__(self):
		print('\n======  {name} ======'.format(name = self.name))
		
		stuff = [a for a in dir(Fighter) if not a.startswith('__')]
		print(stuff)

		for attr in stuff:
			print(attr)

		# print('Health: {hp}'.format(hp = self.health))
		# print('Strength: {str}'.format(str = self.str))
		# print('Health: {hp}'.format(hp = self.health))
		

testUser = Fighter()

testUser.__showStats__()

# testUser.__levelUp()

# testUser.__showStats()
