import time
import player

def adventure():
    print("You are stranded in the middle of the ocean.")
    print("You started this world by falling a good five meters down into the Endless Sea of Cnidaria.")
    print("Luckily the tornado has passed, and the waters are completely still.")
    print("You look around yourself and spot an island nearby.")
    print("You swim towards the island and scout around.")
    print("You see no hostile creatures on the island.")
    print("You can only see some bamboo trees, some big palm trees, some spots of grass and a lot of sand.")
    return first_challenge()

def first_challenge():
    print("What do you want to do now?")
    choice = input("[1] Build a raft, [2] build a mansion like those on youtube or [3] test if something is edible on this island? ")

    if choice == "1":
        print("You successfully build a raft.")

    elif choice == "2":
        print("You try your best to build a mansion.")
        print("You are almost finished.")
        print("Crack.")
        print("You break your ankle, and with no other help in sight you claimed your death.")
        player.hp -= 100

    elif choice == "2":
        print("You try to eat the grass.")
        print("Then you try to eat the bamboo when you die from food poisoning. What an idiot.")
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return first_challenge()


def second_challenge():
    print("You walk around the island, trying to find something else in the horizon.")
    time.sleep(1)
    print("You spot something big in the horizon.")
    time.sleep(1)
    print("East, you can see (pun intended) a great island.")
    time.sleep(1)

    choice = input("Do you wish to [1] travel with the currents to the island or [2] use some driftwood as a paddle to travel faster. ")

    if choice == "1":
        print("You arrive at the island and its dark outside.")
        time.sleep(1)
        print("Find shelter quickly.")
        time.sleep(1)
        return third_challenge_path_1()

    elif choice == "2":
        print("You arrive at the great island before it has turned dark, but you are tired.")
        time.sleep(1)
        return third_challenge_path_2()

!!!!!!!!
def third_challenge_path_1():
    print("Where do you want to sleep?")
    time.sleep(1)
    choice = input("[1] Your raft, [2] in a nearby tree or [3] on the beach near your raft. ")

    if choice == "1":
        print("You woke up in the middle of the ocean.")
        time.sleep(1)
        print("The currents must have dragged you out while you were asleep.")
        time.sleep(1)
        print("A giant shark swooped out of nowhere and killed you.")
        player.hp -= 100

    elif choice == "2":
        print("You managed to sleep well in the tree and nothing bad happened during the night.")
        time.sleep(1)

    elif choice == "3":
        print("During the night you felt a sharp pain in your right arm.")
        time.sleep(1)
        print("Hundreds of crabs have invaded the beach and they are taking you with them, piece by piece.")
        time.sleep(1)
        print("Rest in piece.")
        player.hp -= 100


def third_challenge_path_2():
    print("Explore and check if there are threats nearby.")
    time.sleep(1)
    print("You check in the trees and find no animals living in them.")
    time.sleep(1)
    print("You have a place to sleep, now what do you want to do until it becomes dark")
    time.sleep(1)
    choice = input("[1] Collect leaves to make the sleeping area more comfortable or [2] explore further into the island. ")

    if choice == "1":
        print("You got an excellent sleep, but you are still a bit tired.")

    elif choice == "2":
        print("You explore further into the heart of the island.")
        time.sleep(1)
        print("You suddenly see a warthog in front of you.")
        time.sleep(1)
        print("He has blood around his mouth and he looks right at you.")
        time.sleep(1)
        print("He charges right at you.")
        time.sleep(1)
        print("You run and barely make it away alive.")
        time.sleep(1)
        print("Now you know that a bloodthirsty warthog haunts this part of the island.")
        time.sleep(1)
        player.hp -= 30
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()
        return fourth_challenge_path_2()


def fourth_challenge_path_1():
    print("You are now exploring the island by climbing up the tallest mountain that is close to you.")
    time.sleep(1)
    print("You look over the island and see a couple of fields of grass with no trees.")
    time.sleep(1)
    print("You see some creatures moving there.")
    time.sleep(1)
    print("In the middle of the island you can see a building that resembles a laboratory.")
    time.sleep(1)
    print("You want to go to the laboratory to see if you can find some clues about what this world is.")
    time.sleep(1)
    print("You walk down the mountain.")
    time.sleep(1)
    print("You decide to rest before you go to the middle of the island.")
    time.sleep(1)
    player.hp += 25
    return fifth_challenge_path_1()


def fourth_challenge_path_2():
    print("You look around and see a mountain.")
    time.sleep(1)
    print("You want to see the entire island from a safer distance, so you climb up.")
    time.sleep(1)
    print("You see a couple of fields which have no trees, and you see creatures moving there.")
    time.sleep(1)
    print("After seeing the warthogs, you want to not enter these areas.")
    time.sleep(1)
    print("In the middle of the island you can spot a laboratory.")
    time.sleep(1)
    print("You want to go to the laboratory to get answers about this world.")
    time.sleep(1)
    print("You walk down the mountain, but because you are so tired you stumble and fall down.")
    time.sleep(1)
    player.hp -= 20
    if player.hp <= 0:
        print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
        exit()
    print("You want to get some rest before going to the middle of the island.")
    time.sleep(1)
    print("You go back to your bed and go to sleep.")
    time.sleep(1)
    player.hp += 25
    return fifth_challenge_path_2()


#first path will get the question to go through the grass field or go through the forest. grass field = death bc warthog and if through forest they reach lab
#second path dodges the field and reaches the lab
#after the two lines above they go into the same path at last
#choice to be made, go through door or window
#If door the crabs storm out at you, rest in piece. If through window you land on top of a kitchen counter unscathed
#you see a circular water tank in the middle of the room.
#In the water tank you see a glowing crystal/ pearl thingy that looks like something important that you need.
#There is one problem however, there is alot of crabs, and it looks like they are doing research on the bioluminecent pearl
#There are tools in the kitchen where you stand. Scizzor, sledgehammer and knife
#Destroy water tank and get pearl. sledgehammer is of course correct
#Run away from the crabs
#The crabs are less heat resistant than you.
#The pearl makes it cooler around you.

