import random
import tkinter as tk
from tkinter import simpledialog
from easygui import *


tk.messagebox.Message(master=None, )


ROOT = tk.Tk()

ROOT.withdraw()


text = "Welcome to MakeAIwork Casino. Welke kleur kies je?"
  
# window title
title = "Roulette"
  
# button list
button_list = []
  
# button 1
button1 = "zwart"
  
# second button
button2 = "rood"
  
# appending button to the button list
button_list.append(button1)
button_list.append(button2)

# creating a button box
colorChoice = buttonbox(text, title, choices = button_list)
  
# title for the message box
title = "Message Box"
  
# message 
message = "Je hebt gekozen voor de kleur:  " + colorChoice
  
# creating a message box 
msg = msgbox(message, title)



bank = int(simpledialog.askstring(title="Test",
                                  prompt="Hoeveel wil je inzetten per spin:"))

inzet = int(simpledialog.askstring(title="Test",
                                  prompt="Totaal speelgeld:"))

herhalingen = int(simpledialog.askstring(title="Test",
                                  prompt="Hoeveel herhalingen?:"))

def roulette( colorChoice, bank, inzet, herhalingen):
    #Colorchoice from input black/red
    if colorChoice == "zwart":
        choice = "Black"
    elif colorChoice == "rood":
        choice = "Red"
    else:
        print("Ongeldige keuze")

    newbank = []
    rounds = 0
    # inzet = 10
    totalRounds = []

    while bank > 0:
        randomizer = random.randint(0,1)
         #randomizer link with black/red
        if randomizer == 0:
            result = "Black"
        else:
            result = "Red"
        # randomizer and color choice match
        if result == choice:
            match = True
        else:
            match = False
        #Bank update
        if match == True:
            bank += inzet
            print("Bet won! New Bank ", bank)
        else:
            bank -= inzet
            print("Bet lost! New Bank ",  bank)
        if rounds > herhalingen:
            break

        # number of rounds
        rounds += 1
        print("round ", rounds)
        totalRounds.append(rounds)
        newbank.append(bank)

    msgbox(f"Aantal Rondes  {max(totalRounds)} Je hebt {max(newbank)} euro gewonnen")
        

        
            
roulette( colorChoice, bank, inzet, herhalingen)

    


    


    