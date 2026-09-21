"""
Trents Aventure Toolkit Project | 9/21/2026
This will be a boss fight where you will fight a dragon.
"""

import time

name = input("What is your name? ")
print(f"Hello, {name}! Welcome to The Quest.")
# Intro


time.sleep(4)


print("You find yourself in a cabin on the outskirts of a village. You need to get gear and supplies, you have 25 gold coins to spend at your will.")
gold_coins = 25
# Defining gold whilst setting the stage.


time.sleep(4)


print("You walked to a local pawn shop. You can buy a dragonslaya for 10 gold coins, basher for 5 gold coins, and manapotion for 10 gold coins.")
# Setting a shop for the next bit of code.


time.sleep(4)



pick = input("What would you like to buy? (dragonslaya, basher, manapotion): ")
dragonslaya = 10
basher = 5
manapotion = 10
if pick == "dragonslaya":
    gold_coins -= dragonslaya
elif pick == "basher":
    gold_coins -= basher
elif pick == "manapotion":
    gold_coins -= manapotion
print (f"You now have {gold_coins} gold coins.")
pick = input("What else would you like to buy?(dragonslaya, basher, manapotion): ")
if pick == "dragonslaya":
    gold_coins -= dragonslaya
elif pick == "basher":
    gold_coins -= basher
elif pick == "manapotion":
    gold_coins -= manapotion
print (f"You now have {gold_coins} gold coins.")
# This is the shop section that allows you to spend your gold coins on utility to fight el drago feller. (Uses if statments because it makes my life easier lol.


time.sleep(4)


print("You are now wandering in the Dark Dark Forest Alone, Who will save you when you need it? It is dangerous to be in this territory alone. You hear growling and at first you think its your stomach. You soon realize its MUCH louder than before, you then see it. A MASSIVE dragon, luckily for you, you're well prepared.")

time.sleep(6)

dragon_health = 500
dragon_health -= 100
print("You then swing at the dragon ... A hit!")
print(f"Dragon HP: {dragon_health}")

time.sleep(6)

print("The dragon absolutely firebombs you. Complete incineration, luckily you have fire resistant armour because I, the gamewriter said so.")

time.sleep(6)

dragon_health -= 200
print("You swing again, will you hit or miss.. ! You hit again! This time it was a critical dealing 200 damage!")
print(f"Dragon HP: {dragon_health}")


time.sleep(6)

dragon_health -= 200
print("The dragon trys to cleave you with his dismantle ability stolen from Heian Era Sukuna but unfortunately for him. YOU are the honored one, your limiless technique that you totally didnt rob from Saturo Gojo saves your life and you reflect his black with your blade. This deals the final blow, CHOPPING ITS HEAD CLEAN OFF. Like brisket... mmm.")












