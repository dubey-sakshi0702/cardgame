import random
suit=('HEART','SPADE','DIMOND','CLUB')
rank=('II','III','IV','V','VI','VII','VIII','IX','X','KING','QUEEN','KING','I')
value={'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'JACK':11,'QUEEN':12,'KING':13,'I':14}

class Card:
	
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
		self.value=value[rank]
	def __str__(self):
		return self.rank+" of "+self.suit
class Deck:
	def __init__(self):
		self.all_cards=[]
		for ran in rank:
			for sui in suit:
				create_card=Card(sui,ran)
				self.all_cards.append(create_card)
	def shuffle(self):
		random.shuffle(self.all_cards)
	def deal(self):
		return self.all_cards.pop()
class Player:
	def __init__(self,name):
		self.name=name
		self.all_cards=[]
	def remove_one(self):
		return self.all_cards.pop(0)
	def add_cards(self,new_cards):
		if type(new_cards)==type([]):
			set.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)
		def __str__(self):
			return f'Player{self.name} has {len(self.all_cards)}'
new_deck=Deck()
new_deck.shuffle()
player_one=Player("one")
player_two=Player("two")
for x in range(7):
	player_one.add_cards(new_deck.deal())
	player_two.add_cards(new_deck.deal())
while len(player_one.all_cards) > 0 and len(player_two.all_cards) >0:
	X1=player_two.all_cards.pop().value
	X2=player_one.all_cards.pop().value
	if X1>X2
	
	print()
if len(player_one.all_cards)==0:
	print ("player one wins")
else :
	print("player_two wins")
