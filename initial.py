import inspect 

class Fighter:

	def __init__(self):	
		self.name = "Bob"
		self.level = 1
		self.health = 40
		self.strength = 10
		self.defense = 4
		self.agility = 5
		self.wisdom = 1.2
		self.weapon = 'Typewriter'

	def __setName__(self, n):
		self.name = n

	def __setWeapon__(self, w):
		self.weapon = w

	def __levelUp__(self):
		self.level += 1
		self.health += 2 * self.wisdom
		self.strength += 2.2 * self.wisdom
		self.defense += 1.5 * self.wisdom

	def __showStats__(self):
		print('\n======  {name} ======'.format(name = self.name))
		
		stuff = [a for a in dir(Fighter) if not a.startswith('__')]
		print(stuff)

		for attr in stuff:
			a = attr + " a"
			print(a)

		# print('Health: {hp}'.format(hp = self.health))
		# print('Strength: {str}'.format(str = self.str))
		# print('Health: {hp}'.format(hp = self.health))
		

current_user = Fighter()

print (current_user.__dict__)

n = str(input('\nWhat is your name?  '))

current_user.__setName__(n)

print('''\nAlright {n}, you have to escape the haunted forest
Who left you there? Who knows

  '''.format(n = current_user.name))

print("Just some some beasts and a demon or two...\n\nDon't worry you got this")

print("So what kind of weapon do you want?\n")

w = str(input('be modest  '))

# print(current_user.__dict__)