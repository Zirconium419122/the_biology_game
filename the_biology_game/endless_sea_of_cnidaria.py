import time
import player

def adventure():
    print("You are stranded in the middle of the ocean.")
    input()
    print("You started this world by falling a good five meters down into the Endless Sea of Cnidaria.")
    input()
    print("Luckily the tornado has passed, and the waters are completely still.")
    input()
    print("You look around yourself and spot an island nearby.")
    input()
    print("You swim towards the island and scout around.")
    input()
    print("You see no hostile creatures on the island.")
    input()
    print("You can only see some bamboo trees, some big palm trees, some spots of grass and a lot of sand.")
    input()
    return first_challenge()

def first_challenge():
    print("What do you want to do now?")
    input()

    choice = input("[1] Build a raft, [2] build a mansion like those on youtube or [3] test if something is edible on this island? ")

    if choice == "1":
        print("You successfully build a raft.")
        input()
        return second_challenge()

    elif choice == "2":
        print("You try your best to build a mansion.")
        input()
        print("You are almost finished.")
        input()
        print("Crack.")
        input()
        print("You break your ankle, and with no other help in sight you claimed your death.")
        player.hp -= 100

    elif choice == "2":
        print("You try to eat the grass.")
        input()
        print("Then you try to eat the bamboo when you die from food poisoning. What an idiot.")
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return first_challenge()


def second_challenge():
    print("You walk around the island, trying to find something else in the horizon.")
    input()
    print("You spot something big in the horizon.")
    input()
    print("East, you can see (pun intended) a great island.")
    input()

    choice = input("Do you wish to [1] travel with the currents to the island or [2] use some driftwood as a paddle to travel faster. ")

    if choice == "1":
        print("You arrive at the island and its dark outside.")
        input()
        print("Find shelter quickly.")
        input()
        return third_challenge_path_1()

    elif choice == "2":
        print("You arrive at the great island before it has turned dark, but you are tired.")
        input()
        return third_challenge_path_2()
    
    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return second_challenge()


def third_challenge_path_1():
    print("Where do you want to sleep?")
    input()

    choice = input("[1] Your raft, [2] in a nearby tree or [3] on the beach near your raft. ")

    if choice == "1":
        print("You woke up in the middle of the ocean.")
        input()
        print("The currents must have dragged you out while you were asleep.")
        input()
        print("A giant shark swooped out of nowhere and killed you.")
        player.hp -= 100
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()

    elif choice == "2":
        print("You managed to sleep well in the tree and nothing bad happened during the night.")
        input()
        return fourth_challenge_path_1()

    elif choice == "3":
        print("During the night you felt a sharp pain in your right arm.")
        input()
        print("Hundreds of crabs have invaded the beach and they are taking you with them, piece by piece.")
        input()
        print("Rest in piece.")
        player.hp -= 100
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()

    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return third_challenge_path_1()


def third_challenge_path_2():
    print("Explore and check if there are threats nearby.")
    input()
    print("You check in the trees and find no animals living in them.")
    input()
    print("You have a place to sleep, now what do you want to do until it becomes dark?")
    input()
    
    choice = input("[1] Collect leaves to make the sleeping area more comfortable or [2] explore further into the island? ")

    if choice == "1":
        print("You got an excellent sleep, but you are still a bit tired.")
        input()
        return fourth_challenge_path_2()

    elif choice == "2":
        print("You explore further into the heart of the island.")
        input()
        print("You suddenly see a warthog in front of you.")
        input()
        print("He has blood around his mouth and he looks right at you.")
        input()
        print("He charges right at you.")
        input()
        print("You run and barely make it away alive.")
        input()
        print("Now you know that a bloodthirsty warthog haunts this part of the island.")
        player.hp -= 30
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()
        return fourth_challenge_path_2()
    
    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return third_challenge_path_2()


def fourth_challenge_path_1():
    print("You are now exploring the island by climbing up the tallest mountain that is close to you.")
    input()
    print("You look over the island and see a couple of fields of grass with no trees.")
    input()
    print("You see some creatures moving there.")
    input()
    print("In the middle of the island you can see a building that resembles a laboratory.")
    input()
    print("You want to go to the laboratory to see if you can find some clues about what this world is.")
    input()
    print("You walk down the mountain, but decide to rest before going to the middle of the island.")
    input()
    player.hp += 25
    return fifth_challenge_path_1()


def fourth_challenge_path_2():
    print("You start exploring and see a mountain.")
    input()
    print("You want to see the entire island from a safer distance, so you climb up.")
    input()
    print("You see a couple of fields which have no trees, and you see creatures moving there.")
    input()
    print("After the encounter with the warthogs, you want to not enter these areas.")
    input()
    print("In the middle of the island you can spot a laboratory.")
    input()
    print("You want to go to the laboratory to get answers about this world.")
    input()
    print("You walk down the mountain, but because you are so tired you stumble and fall down.")
    input()
    player.hp -= 20
    if player.hp <= 0:
        print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
        exit()
    print("You get some rest before going to the middle of the island.")
    input()
    player.hp += 25
    return fifth_challenge_path_2()

def fifth_challenge_path_1():
    print("After resting you are met with two paths to your destination, one going through the grass fields while the other goes through a forest.")
    input()

    choice = input("Do you [1] go through the grass field or [2] go through the forest? ")

    if choice == "1":
        print("In the tall grass you suddenly encounter a warthog, killing you on sight.")
        player.hp -= 100
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()

    elif choice == "2":
        print("You go through the forest and reach the laboratory successfully, also avoiding the crabs, good job.")
        input()
        return sixth_challenge()
    
def fifth_challenge_path_2():
    print("Avoiding the open fields (and crabs everywhere), you reach the laboratory successfully.")
    input()
    return sixth_challenge()

def sixth_challenge():

    choice = input("Do you wish to enter [1] through the window or [2] through the door? ")
                   
    if choice == "1":
        print("You jump through the window, landing on top of a kitchen counter, but see tons of crabs crawling on the floor.")
        input()
        return seventh_challenge()

    elif choice == "2":
        print("The place is crawling with crabs (literally), who storm you and cut you into pieces.")
        input()
        print("Rest in piece.")

    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return sixth_challenge()


def seventh_challenge():
    print("You spot a circular water tank in the middle of the room. It contains a glowing pearl, seemingly important.")
    input()
    print("The crabs seem to be doing research on the pearl. To obtain it you may use one of two tools.")
    input()

    choice = input("[1] using a sledgehammer to obtain the pearl then making a run for it or [2] using a knife to defeat the crabs then open the tank. ")

    if choice == "1":
        print(f"You break the glass, take the pearl and get out of there as fast as possible. Good job {player.name}, you have obtained the Bioluminescent Pearl.")
        input()
        print("The crabs are unable to follow due to the great heat, but the Bioluminescent Pearl cools the air around you.")
        input()
        return eighth_challenge()

    elif choice == "2":
        print("You try to kill the crabs, but there are simply too many. What a moron.")
        player.hp -= 200

    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return seventh_challenge()

def eighth_challenge():
    print("You spot a flood in the distance, and in front of you there are three portals. Where d you go now?")
    input()

    choice = input("[1] back to the Islets of Langerhans or [2] back to the abyss of axons? ")

    if choice == "1":
        print("A wise choice.")
        input()

    elif choice == "2":
        print("The flood drowns you and the Sorcerer together.")
        player.hp -=100
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()

    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return eihth_challenge()


# Code for complete game
""""
def eighth_challenge():
    print("You spot a flood in the distance, and in front of you there are three portals. Where d you go now?")
    input()

    choice = input("[1] back to the Islets of Langerhans, [2] back to the abyss of axons or [3] to Pyrexia, the land of fire? ")

    if choice == "1":
        print("The dragons eat you alive as you are not new, nor have you obtained the three items.")
        input()

    elif choice == "2":
        print("The flood drowns you and the Sorcerer together.")
        player.hp -=100
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()

    elif choice == "3":
        print("A wise choice.")
        input()

    else:
        print("Invalid input, please check your spelling and try again.")
        input()
        return eihth_challenge()"""