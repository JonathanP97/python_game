import inspect 

class Fighter:

	def __init__(self):	
		self.name = "Bob"
		self.health = 40
		self.strength = 15
		self.defense = 3

	def __setName__(self, n):
		self.name = n

	def __setStats__(self, hp, st, d):
		self.health = hp
		self.strength = st
		self.defense = d

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

	# add method to check if already dead
	def __was_hit__(self, e):
		dmg_taken = e.strength - self.defense
		self.health -= dmg_taken

		if self.health < 0:
			self.health = 0

		return dmg_taken

	def __attack__(self, e):
		dmg_taken = e.__was_hit__(self)
		print("{user} attacked {ene} for {dmg} damage\n{ene}: {ene_hp} Health\n"
			.format(user = self.name, ene = e.name, dmg = dmg_taken, ene_hp = e.health))

current_user = Fighter()
enemy = Fighter()
enemy.__setStats__(30, 10, 2)
print (current_user.__dict__)

n = str(input('\nWhat is your name?  '))

current_user.__setName__(n)

print(current_user.__dict__)
print(enemy.__dict__)

# while current_user.health != 0 or enemy.health != 0:

while True == True: 
	current_user.__attack__(enemy)
	if(enemy.health == 0):
		print('You win!')
		break

	enemy.__attack__(current_user)
	if(current_user.health == 0):
		print('You lost :c')
		break


