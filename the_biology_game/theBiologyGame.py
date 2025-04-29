import abyss_of_axons
import endless_sea_of_cnidaria
import pyrexia_land_of_fire
import player
import time
# Redundant code that is kept just in case...
# from the_biology_game.player import inventory

player.name = input("Adventurer, please enter your name: ")
print(f"Welcome, {player.name}, you find yourself high in the sky, in the Flying Islets of Langerhans, the land of vicious flying dragons with {player.hp} HP.")
"""time.sleep(8)
print("There is a lot you need to learn about these worlds.")
time.sleep(4)
print("Yes, you heard me correctly, worlds.")
time.sleep(4)
print("There are multiple worlds here and you need to enter every single one of them and collect an item in each world.")
time.sleep(7)
print("To get into these different worlds, you need to go into different portals.")
time.sleep(5)
print("There is a slight problem with these worlds however.")
time.sleep(5)
print("There are extreme natural disasters, and this is also how the worlds are connected.")
time.sleep(6)
print("Every world has the same disasters at the same time.")
time.sleep(5)
print("That is why you need to dodge the disasters in worlds where they can't hurt you and still visit all the worlds.")
time.sleep(8)
print("Right now there is a storm coming, a tornado, and you need to find a safe space.")
time.sleep(6)"""

choice = input("Do you want to go into portal [1] The Endless Sea of Cnidaria, [2] The Abyss of Axons or [3] Pyrexia, the Land of Fire? ")

if choice == "1":
    print("You fall down into a huge ocean and  see the tornado coming closer, ready to destroy anything in its path.")
    print("The tornado comes gets closer and closer...")
    print("And you instantly die from its winds.")
    player.hp -= 100

if choice == "2":
    abyss_of_axons.adventure()
    if player.hp > 0:
        print(f"Congratulations, {player.name}! You have completed the abyss and earned the Neuron Crystal!")
        player.inventory.append("Neuron Crystal")
        player.worlds_visited += 1

if "Neuron Crystal" in player.inventory:
    endless_sea_of_cnidaria.adventure()
    if player.hp > 0:
        print(f"Congratulations, {player.name}! You have completed the Sea of Cnidaria and earned the Bioluminescent Pearl.")
        player.inventory.append("Bioluminescent Pearl")
        player.worlds_visited += 1

if choice == "3":
    print("You suddenly stand in a world full of fire and lava.")
    print("You see the tornado coming closer, it is a fire tornado.")
    print("There is no cover in sight.")
    print("You instantly die from scorching heat.")
    player.hp -= 100

if player.hp <= 0:
    print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
    # Possibly redundant or problematic?
    exit()

if "Neuron Crystal" in player.inventory and "Bioluminescent Pearl" in player.inventory:
    print(f"Congratulations {player.name}, you have won the game!")
    exit()

