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
