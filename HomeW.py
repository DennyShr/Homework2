import random
import csv
class PlayerData():
	player = None
	Player1 = {
	'name': 'Power man',
	'power': 15,
	'skill': 1.0,
	'health': 100,
	}
	Player2 = {
	'name': 'Healthy man',
	'power': 10,
	'skill': 1.0,
	'health': 150,
	}
	Player3 = {
	'name': 'Skill man',
	'power': 10,
	'skill': 2.0,
	'health': 100,
	}

class ChoosingPlayerType(PlayerData):
	def __init__(self, choice):
		self.choice = choice
	def choosing_type(self):
		if self.choice == 1:
			player_type = self.Player1
		elif self.choice == 2:
			player_type = self.Player2
		elif self.choice == 3:
			player_type = self.Player3
		return player_type

class PlayerSelection():
	def choose_your_player(self):
		print('Please select warrior: 1 - strong, 2 - healthy, 3 - skill')
		return int(input('Your choice: '))

class OpponentSelection():
	def opponent_random_choice (self):
		return random.randint(1,3)	

class Fight(PlayerSelection, OpponentSelection):
	def __init__ (self):
		player = ChoosingPlayerType(self.choose_your_player())
		self.player = player.choosing_type()

		opponent = ChoosingPlayerType(self.opponent_random_choice())
		self.opponent = opponent.choosing_type()
	def fight_init_massage (self):
		print('Your warrior: ', self.player['name'])
		print('Opponent: ', self.opponent['name'])
	def fight_main (self):
		player = self.player
		opponent = self.opponent
		win = False
		while True:
			print('Your player HP: ', player['health'])
			print('Opponent    HP: ', opponent['health'], '\n')
			print('Please select kick: 1 - to head, 2 - to body, 3 - to foot = ')
			kick = int(input('You Choice: '))
			print ('Please select block: 1 - to head, 2 - to body, 3 - to foot = ')
			block = int(input('You Choice: '))
			print('\n')
			opponent_kick = random.randint(1,3)
			opponent_block = random.randint(1,3)
			if kick != opponent_block:
				print('You hit an opponent!')
				opponent['health'] = opponent['health'] - (player['power'] * player['skill'])
			if block != opponent_kick:
				print('Opponent hit you :( ')
				player['health'] = player['health'] - (opponent['power'] * opponent['skill'])
			if player['health'] and opponent['health'] <= 0:
				break
			if player['health'] <= 0:
				break
			if opponent['health'] <= 0:
				win = True
				break
		if win:
			print('YOU WINNER!!!')
		else:
			print('GAME OVER.')


fight = Fight()
fight.fight_init_massage()
fight.fight_main()


