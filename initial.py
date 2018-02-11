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

	# Called when fighter is hit 
	# Recieves enemy object and subtracts with defending fighters defense
	def __was_hit__(self, e):
		dmg_taken = e.strength - self.defense
		self.health -= dmg_taken

		if self.health < 0:
			self.health = 0
		
		return dmg_taken

	# Triggers the was_hit method and displays staus info
	# shows health of character who was just hit
	def __attack__(self, e):
		dmg_taken = e.__was_hit__(self)
		print("{user} attacked {ene} for {dmg} damage\n{ene}: {ene_hp} Health\n"
			.format(user = self.name, ene = e.name, dmg = dmg_taken, ene_hp = e.health))

# Simulates battle between two fighter objects
def battle(first, second):
	while True:
		current_user.__attack__(enemy)	
		if(enemy.health == 0):
			print('You win!')
			return first.name

		enemy.__attack__(current_user)
		if(current_user.health == 0):
			print('You lost :c')
			return second.name


# start 
current_user = Fighter()
enemy = Fighter()
enemy.__setStats__(50, 16, 4)

n = str(input('\nWhat is your name?\n'))

current_user.__setName__(n)

print(current_user.name, current_user.health)
print(enemy.name, enemy.health)
print("{user} are you ready?\n".format(user = current_user.name))
	
victor = battle(current_user, enemy)
print(victor, 'won')