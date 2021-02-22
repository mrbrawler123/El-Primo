def common_data(list1, list2): 
    result = False
    for x in list1: 
      for y in list2: 
        if x == y: 
          result = True
          return result
import time
import random
from itertools import product
import string
print("EL PRIMO")
time.sleep(3)
print("This is our own version of 'Uno'. Instead of the colours you will have letters. Also, the special cards have been removed. The rest of the game is the same.")
time.sleep(2)
letter_list1 = list(string.ascii_uppercase)
idontneedthsi = int(input("Enter the number of suites: "))
time.sleep(1)
if idontneedthsi > 26 or idontneedthsi < 2:
	idontneedthsi = int(input("Enter a number less than or equal to 26 and greater than 1: "))
	time.sleep(1)
letter_list = []
time.sleep(1)
for kj in range(idontneedthsi):
	letter_list.append(letter_list1[kj])
time.sleep(1)
s = int(input("Enter the number of cards you want in your deck: "))
time.sleep(1)
while s > len(letter_list) * 5 - 5:
	s = int(input(f"You can have upto {len(letter_list) * 5 - 5} cards in your deck: "))
	time.sleep(1)
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
possible_cards = list(product(num_list, letter_list))
final_possible_cards = []
for x in possible_cards:
	y = "".join(x)
	final_possible_cards.append(y)
player_deck = []
cablan_deck = []
ran_card = ""
for gj in range(s):
	ran_card = random.choice(final_possible_cards)
	player_deck.append(ran_card)
	final_possible_cards.remove(ran_card)
for gh in range(s):
	ran_card = random.choice(final_possible_cards)
	cablan_deck.append(ran_card)
	final_possible_cards.remove(ran_card)
opening_card = random.choice(final_possible_cards)
previouscard = opening_card
ineedthislist = []
print(f"Opening Card: {opening_card}")
time.sleep(1)
while len(cablan_deck) != 0 and len(player_deck) != 0:
	print(f"Your current deck: {', '.join(player_deck)}")
	time.sleep(1)
	for dfg in player_deck:
		dfgl = list(dfg)
		if common_data(dfgl, list(previouscard)) == True:
			break
		else:
			ineedthislist.append(dfg)
	if len(player_deck) == len(ineedthislist):
		rsncard2 = random.choice(final_possible_cards)
		player_deck.append(rsncard2)
		final_possible_cards.remove(rsncard2)
		print("You cannot play a card.")
		time.sleep(1)
	else:
		p = input("Enter your card: ")
		time.sleep(1)
		p = p.upper()
		p_list = list(p)
		previouscard_list = list(previouscard)
		while p not in player_deck or common_data(p_list, previouscard_list) != True:
			p = input("Enter a card in your deck and with a common number or letter: ")
			time.sleep(1)
			p = p.upper()
			p_list = list(p)
		p = p.upper()
		print("Card Successful!")
		time.sleep(1)
		p = p.upper()
		player_deck.remove(p)
		final_possible_cards.append(p)
		previouscard = p
	previouscard_list = list(previouscard)
	neednum = len(cablan_deck)
	for qw in cablan_deck:
		qw_list = list(qw)
		if common_data(qw_list, previouscard_list) == True:
			print(f"Computer's Card: {qw}")
			time.sleep(1)
			cablan_deck.remove(qw)
			final_possible_cards.append(qw)
			previouscard = qw
			break
	if neednum == len(cablan_deck):
		rnafdhdj = random.choice(final_possible_cards)
		cablan_deck.append(rnafdhdj)
		final_possible_cards.remove(rnafdhdj)
		print("The Computer cannot play a card.")
		time.sleep(1)
	print(f"The Computer has {len(cablan_deck)} cards remaning.")
	time.sleep(1)
	ineedthislist = []
time.sleep(1)
if len(cablan_deck) == 0:
	print("The Computer has won!")
if len(player_deck) == 0:
	print("You have won!")
if len(player_deck) == 0 and len(cablan_deck) == 0:
	print("It is a draw!")