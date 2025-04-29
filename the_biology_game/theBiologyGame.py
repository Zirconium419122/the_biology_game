import abyss_of_axons
import endless_sea_of_cnidaria
import pyrexia_land_of_fire
import player
import time
# Redundant code that is kept just in case...
# from the_biology_game.player import inventory

player.name = input("Adventurer, please enter your name: ")
print(f"Welcome, {player.name}, you find yourself high in the sky, in the Flying Islets of Langerhans, the land of vicious flying dragons with {player.hp} HP.")
input()
print("There is a lot you need to learn about these worlds.")
input()
print("Yes, you heard me correctly, worlds.")
input()
print("There are multiple worlds here and you need to enter every single one of them and collect an item in each world to defeat the Supreme Sorcerer.")
input()
print("He is currently manipulating the thoughts of the dragons in these lands, making them friendly towards him but hostile towards all else.") 
input()
print("To get into these different worlds, you need to go into different portals.")
input()
print("There is a slight problem with these worlds however.")
input()
print("There are extreme natural disasters, and this is also how the worlds are connected.")
input()
print("Every world has the same disasters at the same time.")
input()
print("That is why you need to dodge the disasters in worlds where they can't hurt you and still visit all the worlds.")
input()
print("Right now there is a storm coming, a tornado, and you need to find a safe space.")
input()

choice = input("Do you want to go into portal [1] The Endless Sea of Cnidaria, [2] The Abyss of Axons or [3] Pyrexia, the Land of Fire? ")

if choice == "1":
    print("You fall down into a huge ocean and  see the tornado coming closer, ready to destroy anything in its path.")
    input()
    print("The tornado comes closer and closer...")
    input()
    print("And you instantly die from its winds.")
    input()
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
    input()
    print("You see the tornado coming closer, it is a fire tornado.")
    input()
    print("There is no cover in sight.")
    input()
    print("You instantly die from scorching heat.")
    input()
    player.hp -= 100

if player.hp <= 0:
    print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
    # Possibly redundant or problematic?
    exit()

# When the supreme sorcerer is defeated
print("As you pass pass through the portal, the crystal and pearl start glowing. Then they turn into a powerful sword and a pair of boots.")
input()
print("The sword is magical, being able to absorb and reflect spells. The boots on the other hand give you the ability to fly.")
input()
print("You must now utilise these items to defeat the Supreme Sorcerer.")
input()
print("But beware adventurer, he is the most powerful creature in these lands. Therefore you must sneak up on him and trick him like his apprentice once did to you.")
input()

def first_challenge():
    print("Which disguise will you use?")

    choice = input("[1] Iron armour, [2] raggy old clothes or [3] the clothes of a sourcerer apprentice? ")

    if choice == "1":
        print("What did you think was going to happen you moron?")
        input()
        print("The sourcerers capture you and use you for wand practice.")
        input()
        player.hp -= 100

    elif choice == "2":
        print("The Supreme Sorcerer does not use human slaves, you genius. He kills you on sight.")
        player.hp -= 100

    elif choice == "3":
        print("You sneak up behind him as one of his apprentices.")
        input()
        print("\"Put that potion over there, will you?\" He says.")
        input()
        print("You stab the Supreme Sorcerer in the back killing him.")
        input()
        print("Your sword absorbs all his power.")
        input()
        print("His underlings come to his rescue, but stand no chance against you.")
        input()
        print("You receive The Shield of Peace.")
        input()
        player.inventory.append("The Shield of Peace")

first_challenge()

if "Neuron Crystal" in player.inventory and "Bioluminescent Pearl" in player.inventory and "The Shield of Peace" in player.inventory:
    print(f"Congratulations {player.name}, you have established peace in these lands and have won the game!")
    input()
    print("Good job adventurer, you are not a moron.")
    exit()

