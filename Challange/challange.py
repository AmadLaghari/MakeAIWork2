
from tkinter import simpledialog
# I Love Lance & Janice

# =====================
 

# You’ve caught two of your fellow minions passing coded notes back and forth — 
# while they’re on duty, no less! Worse, you’re pretty sure it’s not job-related — 
# they’re both huge fans of the space soap opera “”Lance & Janice””. 
# 
# You know how much Commander Lambda hates waste, 
# so if you can prove that these minions are wasting her time passing non-job-related notes, 
# it’ll put you that much closer to a promotion.
 

# Fortunately for you, the minions aren’t exactly advanced cryptographers. 
# In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], 
# while every other character (including uppercase letters and punctuation) is left untouched. 
# That is, ‘a’ becomes ‘z’, ‘b’ becomes ‘y’, ‘c’ becomes ‘x’, etc. 
# For instance, the word “”vmxibkgrlm””, when decoded, would become “”encryption””.
 

# Write a function called solution(s) which takes in a string and returns 
# the deciphered string so you can show the commander proof that these minions are talking about “”Lance & Janice”” 
# instead of doing their jobs.
 

# Languages

# =========

# To provide a Python solution, edit solution.py

# To provide a Java solution, edit solution.java

# Test cases
# ==========



# Inputs:
decryption_input= "wrw blf hvv ozhg mrtsg’h vkrhlwv?"
encryption_input = "I have solved the puzzle"


#versions
original=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
opposite=['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']


#decryption
def decryption(original, opposite, decryption_input):
    dict = {original[i]: opposite[i] for i in range(len(original))}
    output = "".join([dict.get(c,c) for c in decryption_input])
    return output

print(decryption(original, opposite, decryption_input))


#encryption
def encryption(original, opposite, encryption_input):
    dict = {opposite[i]: original[i] for i in range(len(opposite))}
    output = "".join([dict.get(c,c) for c in encryption_input])
    return output

print(encryption(original, opposite, encryption_input))