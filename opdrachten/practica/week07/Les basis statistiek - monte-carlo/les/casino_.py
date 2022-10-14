import random
import tkinter as tk
from tkinter import simpledialog
from easygui import *

ROOT = tk.Tk()

ROOT.withdraw()


text = "Welcome to MakeAIwork Casino"
  
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
message = "Je hebt gekozen voor de kleir: " + colorChoice
  
# creating a message box 
msg = msgbox(message, title)



# colorChoice = simpledialog.askstring(title="Test",
#                                   prompt="Welke kleur kies je? zwart of rood:")




def roulette( colorChoice):
    #Colorchoice from input black/red
    if colorChoice == "zwart":
        choice = "Black"
    elif colorChoice == "rood":
        choice = "Red"
    else:
        print("Ongeldige keuze")

    bank = 40
    rounds = 0
    inzet = 10

    while bank > 0:
        randomizer = random.randint(0,1)
         #randomizer link with black/red
        if randomizer == 0:
            result = "Black"
        elif:
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
        # number of rounds
        rounds += 1
        print("round ", rounds)
        

        
            
roulette( colorChoice)

    


    


    