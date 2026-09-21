import time

fortnite = "Fortnite"
def tavern_welcome():
    print("Hello Welcome to the Tavern! How are you doing?")
def blacksmith_forge(item):
    print("Your item is being forged.")
    time.sleep(2)
    print("Your item has been forged.")

item = input("What item do you want to forge? ")
blacksmith_forge(item)
blacksmith_forge("Dragon Shield")
def potion_shop(health_potion = 6, mana_potion = 4):
    print("A Mana Potion Costs 4 gold coins and a Health Potion costs 6 gold coins.")

potion_shop(fortnite)
potion_shop(health_potion = 6, mana_potion = 4)