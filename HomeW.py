import random
import csv

class CSVFile():

	FIELDNAMES = ['name','health','power','skill']
	FILENAMES='Warrior.csv'

	def set_headers(self, data):
		with open(self.FILENAMES, 'w', newline='') as file:
			writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES, delimiter=',')
			writer.writerow(data)

	def write(self, data):
		with open(self.FILENAMES, 'a', newline='') as file:
			writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES, delimiter=',')
			writer.writerow(data)

	def read(self):
		with open(self.FILENAMES, 'r') as file:
			reader = csv.DictReader(file, fieldnames=self.FIELDNAMES, delimiter=',')
			return list(reader)

class ChooseType(CSVFile):

	def __init__(self, choice):
		self.choice = choice

	@property
	def schoice(self):
		return self.choice

	@schoice.setter
	def sschoice(self, val):
		if val > 0 and val < 4:
			self.choice = 1
		else:
			self.choice = 3
	
	def choosing_type(self):
		if self.choice == 1:
			player_type = self.read()[1]
		elif self.choice == 2:
			player_type = self.read()[2]
		elif self.choice == 3:
			player_type = self.read()[3]
		return player_type

class PlayerSelection():

	def choose_your_player(self):
		print('Please select warrior: 1 - strong, 2 - healthy, 3 - skill')
		return int(input('Your choice: '))

	def opponent_random_choice (self):
		return random.randint(1,3)	
	
class Fight(PlayerSelection):

	def __init__ (self):
		player = ChooseType(self.choose_your_player())
		self.player = player.choosing_type()
		opponent = ChooseType(self.opponent_random_choice())
		self.opponent = opponent.choosing_type()

	def fight_init_massage (self):
		print('Your warrior: ', self.player['name'])
		print('Opponent: ', self.opponent['name'])

	def fight_main (self):
		player = self.player
		opponent = self.opponent
		p_health = int(player['health'])
		p_power = int(player['power'])
		p_skill = int(player['skill'])
		o_health = int(opponent['health'])
		o_power = int(opponent['power'])
		o_skill = int(opponent['skill'])
		win = False
		while True:
			print('Your player HP: ', p_health)
			print('Opponent    HP: ', o_health, '\n')
			print('Please select kick: 1 - to head, 2 - to body, 3 - to foot = ')
			kick = int(input('You Choice: '))
			print ('Please select block: 1 - to head, 2 - to body, 3 - to foot = ')
			block = int(input('You Choice: '))
			print('\n')
			opponent_kick = random.randint(1,3)
			opponent_block = random.randint(1,3)
			if kick != opponent_block:
				print('You hit an opponent!')
				o_health = o_health - (p_power * p_skill)
			if block != opponent_kick:
				print('Opponent hit you :( ')
				p_health = p_health - (o_power * o_skill)
			if p_health and o_health <= 0:
				break
			if p_health <= 0:
				break
			if o_health <= 0:
				win = True
				break
		if win:
			print('YOU WINNER!!!')
		else:
			print('GAME OVER.')

fight = Fight()
fight.fight_init_massage()
fight.fight_main()

data = CSVFile()
my_warrior = data.read()[fight.choose_your_player()]
opponent_warrior = data.read()[fight.opponent_random_choice()]
class PlayersComparison():

	def __init__(self, name, health, power):
		self.name = name
		self.power = int(power)
		self.health = int(health)
	def __str__(self):
		return 'Name: {}, Health: {}, Power: {}.'.format(self.name, self.health, self.power)
	def __gt__(self, opponent):
		print(self)
		print(opponent)
		if self.health > opponent.health:
			print('You have more Health')
		elif self.health == opponent.health:
			print('Same Health')
		else:
			print('You have less Health')
		if self.power > opponent.power:
			print('You have more Power')
		elif self.power == opponent.power:
			print('Same Power')
		else:
			print('You have less Power')

warrior1 = PlayersComparison(my_warrior['name'], my_warrior['health'], my_warrior['power'])
warrior2 = PlayersComparison(opponent_warrior['name'], opponent_warrior['health'], opponent_warrior['power'])

print(warrior1 > warrior2)