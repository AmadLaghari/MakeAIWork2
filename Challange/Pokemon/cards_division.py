import random
from data import all_cards
from easygui import *

computer_cards = []

title = "Pokemon Fight"
textChoseCards = "Welkom bij Pokemon Trading spel. Kies 5 kaarten"
button_list =  list(all_cards.keys())
cards = multchoicebox(textChoseCards, title, button_list)
if len(cards) != 5:
        indexbox("Je hebt geen 5 kaarten gekozen. Wil je toch doorgaan?")


randomNumbers = random.sample(range(10), 5)
for x in randomNumbers:
    fiveCards = button_list[x]
    computer_cards.append(fiveCards)