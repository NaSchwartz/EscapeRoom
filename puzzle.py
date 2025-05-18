import os, time
from random import randint
import deck_tools

deck = deck_tools.createdeck(True)

#print(deck_tools.deal_whole_deck(4, deck))

print(deck_tools.partial_deall(4, 2, deck))
print(deck)
