import tkinter as tk
from tkinter import simpledialog
from easygui import *
import panel as pn
from data import all_cards
from cards_division import computer_cards, cards
import random




class Pokemon():
    def __init__(self, all_cards, computer_cards, cards, remaining_health: list= [], remaining_health_computer: list= []):
        self.remaining_health = remaining_health
        self.remaining_health_computer= remaining_health_computer
        self.all_cards = all_cards
        self.computer_cards = computer_cards
        self.cards = cards
    

    
    def pokemonFight(self):
        for x in range(len(self.cards)):
            # Keuze menu
            player_main_card = buttonbox('Kies jouw main card', "Pokemon Fight", choices = self.cards)

            # Berekening Aanval, aantal keer aanvallen en Health van player kaarten
            player_health = self.all_cards.get(player_main_card)[0]
            player_attack = self.all_cards.get(player_main_card)[1]
            player_attack_rounds = (player_health/player_attack)/2

            # Berekening Aanval, aantal keer aanvallen en Health van computer kaarten
            computer_main_card = self.computer_cards[random.randint(0, 3)]
            computer_health = self.all_cards.get(computer_main_card)[0]
            computer_attack = self.all_cards.get(computer_main_card)[1]
            computer_attack_rounds = (computer_health/computer_attack)/2

            # Aanval op computer kaart
            new_computer_health = computer_health - (player_attack_rounds * player_attack)
            msgbox(f"(Jouw){player_main_card} heeft (Computer){computer_main_card} aangevallen. De nieuwe computer health is: {new_computer_health}")
            self.remaining_health_computer.append(new_computer_health)

            # Aanval op player kaart
            new_player_health = player_health - (computer_attack_rounds * computer_attack)
            cards.remove(player_main_card)
            msgbox(f"(Computer){computer_main_card} heeft (Jouw){player_main_card} aangevallen aan! Je nieuwe health is: {new_player_health}")
            self.remaining_health.append(new_player_health)


    def result(self):
        # resultaat berekenen aan de hand van wie meeste schade heeft gekregen
        if sum(self.remaining_health) > sum(self.remaining_health_computer):
            msgbox("Jij hebt gewonnen")
        elif sum(self.remaining_health_computer) >sum(self.remaining_health):
            msgbox("Computer heeft gewonnen")
        else:
            msgbox("Gelijk gespeeld")


fight = Pokemon(all_cards, computer_cards, cards).pokemonFight()
result = Pokemon(all_cards, computer_cards, cards).result()



