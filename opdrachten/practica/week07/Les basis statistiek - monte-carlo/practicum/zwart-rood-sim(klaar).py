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
button1 = "Zwart"
  
# second 2
button2 = "Rood"
  
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
                                  prompt="Totaal speelgeld:"))

herhalingen = int(simpledialog.askstring(title="Test",
                                  prompt="Aantal herhalingen?:"))

inzet = int(bank)/int(herhalingen)

msgbox(f"Inzet per spin: {int(inzet)} euro \n {herhalingen} herhalingen op de kleur: {colorChoice}")

def roulette( colorChoice, bank, inzet, herhalingen):
    #Colorchoice from input black/red
    if colorChoice == "Zwart":
        choice = "Black"
    elif colorChoice == "Rood":
        choice = "Red"
    else:
        print("Ongeldige keuze")

    newbank = []
    rounds = 1
    # inzet = 10
    totalRounds = 1
    lost = []
    totalLost = 0
    totalWon = 0
    totalBank = bank 

    while bank > 0:
        randomizer = random.randint(0,1)
         #randomizer link with black/red
        if randomizer == 0:
            result = "Black"
        else:
            result = "Red"
        # randomizer and color choice match
        # Bank update
        if result == choice:
            bank += inzet
            print("Bet won! New Bank ", bank)
            totalWon += 1
        else:
            bank -= inzet
            print("Bet lost! New Bank ",  bank)
            totalLost += 1
        if rounds >= herhalingen :
            break
        elif bank <= 0:
            msgbox(f"Speelgeld: 0 euro. U heeft alles verloren")
            lost.append(1)
        else:
            print("round ", rounds)
            totalRounds += 1
            newbank.append(bank)
        # number of rounds
        rounds += 1
    newbankValue = round(newbank[-1],2)
    win =  round((newbankValue - totalBank),2)
    lose =  round((totalBank - newbankValue),2)
    print(lose)

    if win> 0 or win == 0: 
        if bank > 10:
            msgbox(f" \n Ronden: {totalRounds} \n Jouw Bank {newbankValue} euro \n Aantal keer gewonnen: {totalWon} \n Aantal keer verloren: {totalLost} \n Totale inzet: {totalBank} euro \n \n Gefeliciteerd! Je hebt {win} euro gewonnen!  ")
    elif win < 0:
        if bank > 10:
            msgbox(f"\n Ronden  {totalRounds} \n Jouw Bank {newbankValue} euro \n Aantal keer gewonnen: {totalWon} \n Aantal keer verloren: {totalLost} \n Totale inzet: {totalBank} euro \n \nHelaas! Je hebt {lose} euro verloren  ")



        
            
roulette( colorChoice, bank, inzet, herhalingen)

    


    


    