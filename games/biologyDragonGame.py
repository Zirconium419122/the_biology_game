import random
import time

def displayIntro():
    print("You are in The Islets of Langerhans, the land of vicious fire-breathing dragons."
          "In front of you, you see three caves."
          "1-The Abyss of Axons"
          "2-The Endless Sea of Cnidaria"
          "3-Pyrexia, the land of fire"
          "In one cave, the dragon is friendly and will share its treasure with you. "
          "The other dragons are greedy and hungry, and will eat you on sight.")

    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2" and cave != "3":
        print("Which cave will you go into? (1, 2 or 3)")
        cave = input()

    return cave

def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)

    viciousCave = random.randint(1,3)

    if chosenCave == str(viciousCave):
        print("Gobbles you down in one bite!")
    else:
        print("Gives you his treasure!")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()

