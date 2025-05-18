
# Creation and display
def createdeck(jokers = False):
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for i in range(suits):
        for j in range(ranks):
            deck.append(f"{ranks[i]} {suits[ij]}") 
    if jokers:
        deck.append("Jok")
        deck.append("Jok")
    return deck

def hand_ToString(player_hand):
    desc = ""
    for card in player_hand:
        desc += card + "  "
    return desc

def pop_card(deck):
    return deck.pop(0)

def deal_whole_deck(number_of_hands : int):
    list_of_hands = []*number_of_hands
    for i in range(number_of_hands):
        