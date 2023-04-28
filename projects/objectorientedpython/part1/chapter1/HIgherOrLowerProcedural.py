import random

# card constants
SUIT_TUPLE= ('Spades','Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9',
  '10', 'Jack', 'Queen', 'King')

NCARDS = 8

#PASS IN DECK AND RETURN A RANDOM CARD FROM DECK
def getCard(deck_list):
    this_card = deck_list.pop()
    return this_card

#returns a shuffled copy of the card
def shuffle(deck_list):
    deck_list_out = deck_list.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

starting_deck_list = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        card_dict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        starting_deck_list.append(card_dict)

score = 50


while True:
    print()
    game_deck_list = shuffle(starting_deck_list)
    
    curr_card_dict = getCard(game_deck_list)
    
    curr_card_rank = curr_card_dict['rank']
    
    currentCardValue = curr_card_dict['value']
    currentCardSuit = curr_card_dict['suit']    
    print('Starting card is:', curr_card_rank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):   # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' + 
                               curr_card_rank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # force lower case
        nextCardDict = getCard(game_deck_list)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15          

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        curr_card_rank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break

print('OK bye')