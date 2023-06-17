import random
import time

def linebreak(sec=2):
	print('\n' + '*'*60 + '\n' + '*'*60 + '\n')
	time.sleep(sec)

# Lists for card variables to generate any of the possible 52 cards
suit_list = ['clubs', 'diamonds', 'hearts', 'spades']
value_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


# Returns a list which represents a random card
# The 0 index represents the card value (e.g. Ace, 6, King, etc.)
# The 1 index represents the card suit (e.g. clubs)
def rand_card():
	rand_suit = random.choice(suit_list)
	rand_value = random.choice(value_list)
	return [str(rand_value), rand_suit]

# Takes a card (represented by a list object in the form [value, suit]) argument
# Gets the value of the card
def get_card_value(card):
	return card[0]
# Gets the suit of the card
def get_card_suit(card):
	return card[1]


# Tells player the hand they have been dealt via print statement
# Prevents repeat cards from being played
# Returns the player's hand, represented by a list of lists'
def deal_player():
	print('\nYou are dealt the following five cards:')
	player_hand = []
	i = 0
	while i < 5:
		letters_list = ['a', 'b', 'c', 'd', 'e']
		given_card = rand_card()
		if given_card not in player_hand:
			print(' %s)   %s of %s' %(letters_list[i], get_card_value(given_card), get_card_suit(given_card)))
			player_hand.append(given_card)
			i = i + 1
	return player_hand


# Returns the number of cards the player wishes to discard
# Error handling ensures only 0-3 cards are discarded
def discard_cards():
	time.sleep(4)
	print('\nYou may choose to discard up to 3 cards for new ones.')
	print('How many cards do you wish to swap (0-3)?')
	while True:
		try:
			discard_x_cards = int(input('\n> '))
			if valid_discard_num(discard_x_cards):
				break
			else:
				print('That is not allowed. Please choose between 0 and 3 cards to discard.')
		except ValueError:
			print('Invalid command. Input a number between 0-3.')
	return discard_x_cards


# Returns True only when the player chooses to discard between 0-3 cards		
def valid_discard_num(discard_num):
	if 0 <= discard_num <= 3:
		return True


# Asks the user to specify what card(s) (a-e) are to be discarded one at a time
# If no cards are to be discarded, then the function returns None
# Otherwise, the function returns a list of lower-case letters (representing cards) to be discarded
def specify_discard_cards(tot_discarded_cards):
	if tot_discarded_cards == 0:
		print('\nYou choose to stick with the hand you were dealt.')
		time.sleep(2)
		return [] # empty list, represents no cards
	else:
		print('The number of cards to be discarded is %s' % tot_discarded_cards)
		time.sleep(2)
		discard_card_list = []
		
		i = 0
		while i < tot_discarded_cards:
			print('\nType the letter of card #%s to be discarded. (a-e)' % (i+1))
			discard_card = input('> ').lower()
			if not valid_card_letter(discard_card):
				continue
			if not check_card_exists(discard_card, discard_card_list):
				continue
				
			discard_card_list.append(discard_card)
			i = i + 1
		return discard_card_list


# Returns True if player inputs a letter between a-e (representing one card from the player's hand)
# Returns False plus a printed info message if the user does not type a valid letter
# Uses inputted letter as an argument
def valid_card_letter(letter_input):
	five_letters = ['a', 'b', 'c', 'd', 'e']
	if letter_input.lower() not in five_letters:
		print("That's not allowed. Choose one card with an assigned letter (a-e)")
		return False
	else:
		return True
				
# Returns True if the user hasn't already chosen a letter representing a card to discard
# Returns False and a printed info message if the user chooses the same card to discard again
# First argument is the inputted letter. Second argument is a list of already inputted letters
def check_card_exists(letter_input, used_letters):
	if letter_input.lower() not in used_letters:
		return True
	else:
		print('You already chose to discard this card. What else will you discard?')
		return False
		

# Returns a preliminary list of identified cards ([value, suit]) to be discarded
# First argument is list of requested discard cards.
# Second argument is the list representing players hand
def identify_discard_cards(discard_list, player_hand):
	cards_to_remove = []
	for letter in discard_list:
		if letter == 'a':
			cards_to_remove.append(player_hand[0])
		if letter == 'b':
			cards_to_remove.append(player_hand[1])
		if letter == 'c':
			cards_to_remove.append(player_hand[2])
		if letter == 'd':
			cards_to_remove.append(player_hand[3])
		if letter == 'e':
			cards_to_remove.append(player_hand[4])
	return cards_to_remove
			

# Removes the cards the player wished to discard from the player's hand
# Functions by creating a prelminary discard list, then compares to player's hand to remove the right cards
# Returns what remains of the player's hand
def throw_discard_cards(discard_list, player_hand, cards_to_chuck):
	for card in cards_to_chuck:
		if card in player_hand:
			player_hand.remove(card)
	return player_hand		

# Returns the player's hand of 5 cards with any new cards drawn
# The object returned is a list of 5 cards (each represented as [value, suit])
# Ensures that no new cards are repeats of what was already in the player's hand
# Prints the hand for the player to see
def receive_new_cards(num_discard_cards, player_hand, cards_to_chuck):
	i = 0
	while i < num_discard_cards:
		received_card = rand_card()
		if received_card not in player_hand and received_card not in cards_to_chuck:
			player_hand.append(received_card)
			i = i + 1
	linebreak()
	print('\nYour final hand is as follows:\n')
	time.sleep(2)
	for card in player_hand:
		print('   %s of %s' % (card[0], card[1]))
	return player_hand
	

# Returns the player's hand in the order of value (Aces low, Kings high)
# Player's hand is a list of lists
# 1st argument is the player's hand, a list of cards (card is itself in the form [value, suit])
# 2nd argument is the list of values ordered from Ace low to King high
def order_card_values(player_hand, value_list):
	ordered_hand = []
	for value in value_list:
		for card in player_hand:
			try:
				# NOTE: All values are currently strings.
				# Any string which can be an integer MUST be converted to an integer
				# The reason is related to problems with comparing values in the value_list against string numbers
				if int(card[0]) == value:
					ordered_hand.append(card)
			except ValueError:
				# The except captures all the string values (i.e. A, J, Q, K)
				if card[0] == value:
					ordered_hand.append(card)
	return ordered_hand


# Function required in the is_straight() function
# Returns a list of two strings
# Strings are the concatenated values of the player's cards
# One string has aces on left, other on right (e.g. ['AA49Q', '49QAA'])
# Cards have already been ordered using the order_card_values function
# Argument is the player's hand in an ordered state
def concatenate_player_values(ordered_hand):
	player_values = []
	for card in ordered_hand:
		player_values.append(str(card[0]))
	
	low_aces_values_str = ''.join(player_values)
	# Represents a concateneated string of card values, already ordered starting with aces
	
	trailing_aces = ''
	for letter in low_aces_values_str:
		if letter == 'A':
			trailing_aces += 'A'
			# Creates a string with a trail of aces which will be added to the raw string later
	high_aces_values_str = low_aces_values_str[len(trailing_aces):] + trailing_aces
	# removes the prefix aces from the values string and places aces at the end of said string
	# e.g. 'AA37K' becomes '37KAA'
	
	return [low_aces_values_str, high_aces_values_str]
		


# Returns True if a STRAIGHT (sequential values) is present in the player's hand
# Otherwise returns False
# Uses the concatenate_player_values function
def is_straight():
	ordered_values_list = concatenate_player_values(ordered_hand)
	for string in ordered_values_list:
		if string in 'A2345678910JQKA':
			return True
	else:
		return False

# Returns True if all cards are of the same suit; FLUSH
# Argument is the hand of the player; a list of cards represented [value, suit]
def is_flush(player_hand):
	player_hand_suit_list = []
	for card in player_hand:
		player_hand_suit_list.append(card[1])
	if player_hand_suit_list[1:] == player_hand_suit_list[:-1]:
		return True
	else:
		return False

# Checks for duplicate card values within the player's hand (arg)
# Counts the duplicate values
# Returns a list of lists; individual lists have two items
# The individual lists are in the form [card value, duplicated x times]
# e.g. [['A', 2], [10, 2]] is a pair of Aces and a pair of 10s
# Further code makes sure no one value is counted more than once
def check_dup_values(player_hand):
	values_list = []
	for card in player_hand:
		values_list.append(card[0])
	
	counted_values = []
	already_checked_value = []
	for value in values_list:
		if value not in already_checked_value:
			already_checked_value.append(value)
			if values_list.count(value) == 2:
				counted_values.append([value, 2])
			if values_list.count(value) == 3:
				counted_values.append([value, 3])
			if values_list.count(value) == 4:
				counted_values.append([value, 4])
	
	return counted_values


# Stores the returned list from check_dup_values(player_hand) as a variable
# Returns the type of hand the player has on the basis of duplicate value cards
def compute_dup_values(player_hand):
	duplicate_values_list = check_dup_values(player_hand)
	
	if len(duplicate_values_list) == 0:
		# No duplicate values
		return False
	
	if len(duplicate_values_list) == 1:
		for mini_list in duplicate_values_list:
			if mini_list[1] == 4:
				return 'FOUR OF A KIND'
			if mini_list[1] == 3:
				return 'THREE OF A KIND'
			if mini_list[1] == 2:
				return 'PAIR OF ' + str(mini_list [0]) + 's'
	
	if len(duplicate_values_list) == 2:
		# Must be TWO PAIRS or FULL HOUSE
		for mini_list in duplicate_values_list:
			if mini_list[1] == 3:
				return 'FULL HOUSE'
		
		pair_list = []
		for mini_list in duplicate_values_list:
			pair = str(mini_list[0])+ 's'
			pair_list.append(pair)
		return 'TWO PAIRS OF ' + pair_list[0] + ' AND ' + pair_list[1]

# Retruns the type of hand the player has
# Ranked/Checked in order of best to worst hand
def determine_hand(player_hand):
	processed_duplicates = compute_dup_values(player_hand)
	if is_straight() and is_flush(player_hand):
		return 'STRAIGHT FLUSH'
	elif processed_duplicates == 'FOUR OF A KIND':
		return 'FOUR OF A KIND'
	elif processed_duplicates == 'FULL HOUSE':
		return 'FULL HOUSE'
	elif is_flush(player_hand):
		return 'FLUSH'
	elif is_straight():
		return 'STRAIGHT'
	elif processed_duplicates == 'THREE OF A KIND':
		return 'THREE OF A KIND'
	elif processed_duplicates:
		return processed_duplicates
	else:
		return determine_high_card(player_hand)

# Returns the highest value card the player has when the best hand is HIGH CARD
# Aces are treated as highest value
# For remainder of value list, highest values are proportional with the inverse of the value_list
def determine_high_card(player_hand):
	reversed_value_list = value_list[::-1]
	for value in reversed_value_list:
		for card in player_hand:
			if card[0] == 'A':
				return 'HIGH CARD ACE'
			if card[0] == value:
				return 'HIGH CARD ' + str(value)

# Returns a list with two items
# First item is the name of the hand the opponent has been assigned
# Second item is a list with 2 values that will provide the "strength" for certain types of hands
# Creates a 'hand' for the principal opponent
# DOES NOT function in the same way as the player's hand
# Instead based on probability to assign the computer with a hand, much simpler!
def opponent_hand(value_list):
	rand_num = random.randint(0, 1000)
	
	opponent_value_cards = []
	i = 0
	# Creates the list of two values that will make up the second item of the return
	while i < 2:
		rand_value = random.choice(value_list)
		if rand_value not in opponent_value_cards:
			opponent_value_cards.append(rand_value)
			i += 1
	
	# Assigns the 'hand' which makes up the first item of the return
	if rand_num <= 300:
		# Overwrites previously assigned first item in oppponent_value_cards list to ensure value is >= 7
		opponent_value_cards[0] = str(random.choice(value_list[6:] + ['A']))
		opp_hand = 'HIGH CARD ' + opponent_value_cards[0]
	elif rand_num <= 700:
		opp_hand = 'PAIR OF ' + str(opponent_value_cards[0]) + 's'
	elif rand_num <= 900:
		opp_hand = 'TWO PAIRS (' + str(opponent_value_cards[0]) + 's AND ' + str(opponent_value_cards[1]) + 's)'
	elif rand_num <= 950:
		opp_hand = 'THREE OF A KIND (' + str(opponent_value_cards[0]) + 's)'
	elif rand_num <= 975:
		opp_hand = 'STRAIGHT'
	elif rand_num <= 987:
		opp_hand = 'FLUSH'
	elif rand_num <= 995:
		opp_hand = 'FULL HOUSE (THREE ' + str(opponent_value_cards[0]) + 's AND TWO ' + str(opponent_value_cards[1]) + 's)'
	elif rand_num <= 999:
		opp_hand = 'FOUR OF A KIND (' + str(opponent_value_cards[0]) + 's)'
	else:
		opp_hand = 'STRAIGHT FLUSH'
	
	return [opp_hand, opponent_value_cards]

def play_again():
	print('\nWould you care to play another round? (y/n)')
	if input('> ').lower() in ['yes', 'y']:
		return True
	else:
		return False
			
#---------GAME LOOP---------#
linebreak(0)
print('-'*15 + "Anthony Starkey's Python Poker" + '-'*15)
linebreak()
print('\nYou play British Poker against an exceptionally skilled player.')
while True:
	time.sleep(3.5)
	dealt_hand = deal_player()
	
	tot_discarded_cards = discard_cards()
	discarded_cards_list = specify_discard_cards(tot_discarded_cards)
	cards_to_chuck = identify_discard_cards(discarded_cards_list, dealt_hand)
	remaining_hand = throw_discard_cards(discarded_cards_list, dealt_hand, cards_to_chuck)
	
	new_hand = receive_new_cards(tot_discarded_cards, remaining_hand, cards_to_chuck)
	ordered_hand = order_card_values(new_hand, value_list)
	
	name_player_hand = determine_hand(ordered_hand) #--> A function which will determine the name of the hand (e.g. FLUSH)
	
	time.sleep(4)
	print('\nYou reveal your hand:\n%s' % name_player_hand)
	time.sleep(3)
	enemy_hand = opponent_hand(value_list)
	print('\nYour opponent reveals their hand:\n' + enemy_hand[0])
	
	#who_wins()
	
	if not play_again():
		print('\nThank you for playing!')
		time.sleep(1)
		break
		
	linebreak()
