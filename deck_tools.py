from random import shuffle


def createdeck(jokers = False):
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for i in range(len(suits)):
        for j in range(len(ranks)):
            deck.append(f"{ranks[j]} {suits[i]}") 
    if jokers:
        deck.append("Jok")
        deck.append("Jok")
    return deck


def pisplay_hand(player_hand):
    desc = ""
    for card in player_hand:
        desc += card + "  "
    return desc


# Dealing out the entire deck
def deal_whole_deck(hand_count : int, deck):
    hands = [[] for i in range(hand_count)]
    ptmp = 0
    while True:
        if deck == []:
            break
        hands[ptmp].append(deck.pop(0))
        ptmp = (ptmp + 1) % hand_count
    
    return hands

# Dealing out part of the deck
def partial_deall(hand_count : int, cards_per_player : int, deck):
    hands = [[] for i in range(hand_count)]
    try:
        for i in range(cards_per_player):
            for hand in hands:
                hand.append(deck.pop(0))

    except:
        print(f"Not enough cards to give all {hand_count} players {cards_per_player} cards!")
        exit()
    
    return hands
