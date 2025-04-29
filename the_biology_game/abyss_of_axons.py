import time
import player


def adventure():
    print("You fall down from the sky and landed on a circular island next to a chasm.")
    time.sleep(1)
    print("You have landed in the Abyss of Axons.")
    time.sleep(1)
    print("You look over the edge and can only see black down into the chasm.")
    time.sleep(1)
    print("It looks like an infinite drop, but it is impossible to tell.")
    time.sleep(1)
    print("You look around, it is completely flat and the Island is around 50 meters in radius.")
    time.sleep(1)
    print("You look into the distance and see the tornado coming fast.")
    time.sleep(1)
    """return first_challenge()

def first_challenge():
    print(f"You are left with the decision, {player.name}")
    time.sleep(1)

    choice = input("Do you wish to [1] stay on the surface and try to survive the tornado or [2] jump into the chasm which seemingly doesn't have a bottom? ")

    if choice == "1":
        print("You choose to stay on top of the island and look around.")
        time.sleep(1)
        print("There is absolutely no cover that you can see.")
        time.sleep(1)
        print("It hits you and drags you around and around before you get flung out the side of it.")
        time.sleep(1)
        print("You look towards the tornado, it grows and grows the closer it gets.")
        time.sleep(1)
        print("It gets closer and you brace for impact.")
        time.sleep(1)
        player.hp -= 100
        print(f"You now have {player.hp} HP.")

    elif choice == "2":
        print("You jump down into the abyss.")
        time.sleep(1)
        print("You fall faster and faster.")
        time.sleep(1)
        print("You can only hear the wind sweeping by your ears as you are falling.")
        time.sleep(1)
        print("You start seeing black and white.")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("You suddently slow down from falling.")
        time.sleep(1)
        print("You look down and see the ground a meter below you.")
        time.sleep(1)
        print("You fall down the last meter and land.")
        time.sleep(1)
        print(f"You have hit the bottom of the abyss unscathed {player.name}!")
        time.sleep(1)
        print("Congratulations adventurer, you have passed your first test.")
        time.sleep(1)
        return second_challenge_text()

    else:
        print("Invalid input, please check your spelling and try again.")
        return first_challenge()


def second_challenge_text():
    print("An old man is standing in front of you looking right at you.")
    time.sleep(1)
    print("He needs your help.")
    time.sleep(1)
    print("A dragon has burned down his house and he needs help collecting more wood.")
    time.sleep(1)
    print("There is wood in the eastern caves.")
    time.sleep(1)
    return second_challenge()


def second_challenge():

    choice = input("Do you want to [1] help the old man or [2] not today? ")

    if choice == "2":
        print("\"A curse has fallen upon you,\" the old man yells. Suddenly, lightning strikes you.")
        player.hp -= 30
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()
        print("Are you sure of your decision")
        print(f"You now have {player.hp} HP, but must still complete the task.")
        return second_challenge()

    elif choice == "1":
        print("\"Thank you, adventurer.\", the old man says.")
        return third_challenge()

    else:
        print("Invalid input, please check your spelling and try again.")
        return second_challenge()


def third_challenge():

    choice = input("You must now choose where to go, [1] north, [2] south, [3] east or [4] west? ")

    if choice == "1":
        print("You get instantly eaten by a hungry dragon.")
        player.hp -= 100

    elif choice == "2":
        print("Venomous snakes kill you with their poison.")
        player.hp -= 100

    elif choice == "3":
        print("You arrive at your destination.")
        return fourth_challenge()

    elif choice == "4":
        print("You arrive at the western caves, notorious for their extreme radiation which kills in an instant (although extremely painfully).")
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return third_challenge()


def fourth_challenge():

    choice = input("Choose your tool: [1] an axe, [2] a very sharp sword or [3] a sharp hilt that can cut through anything. ")

    if choice == "1":
        print("You aquire the necessary wood and bring it back to the old man.")
        return fifth_challenge_text()

    elif choice == "2":
        print("The sword quickly dulls and gets stuck in the tree. While trying to get it out, the tree falls on you killing you.")
        player.hp -= 100

    elif choice == "3":
        print("The hilt is so sharp that it cuts your hand like (read with british accent) butter and you die from bleeding.")
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return fourth_challenge()


def fifth_challenge_text():
    print("\"Can you please get me some food.\"")
    time.sleep(1)
    print("\"The dragon has stolen all of my, which I need to survive.\"")
    time.sleep(1)
    print("\"The dragon's lair is in the northern caves.\"")
    time.sleep(1)
    print("\"It is important that the dragon does not see you, because he will eat you alive if he does.\"")
    time.sleep(1)
    return fifth_challenge()


def fifth_challenge():

    choice = input("Do you want to [1] steal the food back from the dragon, [2] \"give me some time so I can decide\" or [3] \"I would never\"? ")

    if choice == "1":
        print("You sneak to the northern caves, dodging the dragons vision.")
        return sixth_challenge()

    elif choice == "2":
        print("\"Please, decide quickly, I have not eaten in days.\"")
        return fifth_challenge()

    elif choice == "3":
        print("\"A great curse shall fall upon you and your family!\" The old man screams. Immediately a big rock falls down on your left arm so you lose it, you were lucky it was not your dominant.")
        player.hp -= 50
        if player.hp <= 0:
            print(f"💀{player.name}, you lost all your HP and have been defeated.💀")
            exit()
        print(f"Now you have {player.hp} HP left, so...")
        return fifth_challenge()

    else:
        print("Invalid input, please check your spelling and try again.")
        return fifth_challenge()


def sixth_challenge():
    print("You are getting close to the food when you hear shifting in the grass behind you...")
    time.sleep(2)

    choice = input("Choose between [1] hiding in the grass or [2] hiding behind a rock. ")

    if choice == "1":
        print("The dragon can clearly see you in the short grass, killing you on sight.")
        player.hp -= 100

    elif choice == "2":
        print("You hide behind a rock and the dragon walk right past you. What an idiot.")
        return seventh_challenge()

    else:
        print("Invalid input, please check your spelling and try again.")
        return sixth_challenge()


def seventh_challenge():
    print("You wait for the dragon to leave your surroundings and start walking towards where the food is.")
    time.sleep(1)
    print("You move closer and you can start smelling the food.")
    time.sleep(1)
    print("You move closer to the food and see the dragons lair, but you do not see the food. Now you are met with yet another choice.")
    time.sleep(1)
    choice = input("Do you [1] go into the dragons lair or [2] run away? ")

    if choice == "1":
        print("You travel further into the dragons lair.")
        time.sleep(1)
        return eighth_challenge()

    elif choice == "2":
        print("You hear the Old man's words in your head \"You dare not help me, curse you!!!\"")
        time.sleep(1)
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return seventh_challenge()


def eighth_challenge():
    print("You move closer to a corner, you can smell that the food is extremely close now...")
    time.sleep(1)
    print("You turn the corner just to stand in front of the food...")
    time.sleep(1)
    print("and the DRAGON!!")
    time.sleep(1)
    print("He looks you in your eyes and asked, \"Why are you here, mere mortal.\" ")
    time.sleep(1)

    choice = input("[1] \"I am here to take back the food you thief!\", or [2] \"Ehm... nothing, I was just walking by.\" ")

    if choice == "1":
        print(f"\"You dare think that you even have a chance at defeating me {player.name}!\"")
        time.sleep(1)
        return ninth_challenge()

    elif choice == "2":
        print("\"There is only one person in this world, the Sorcerer.\"")
        time.sleep(1)
        print("\"I KNOW YOUR WEAKNESS!\"")
        time.sleep(1)
        print("\"FIRE!!!\"")
        time.sleep(1)
        print(f"Your \"confidence\" in yourself killed you {player.name}, literally.")
        time.sleep(1)
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return eighth_challenge()


def ninth_challenge():
    print("\"Yes, I will walk away from here with the food, regardless of the outcome on your part.\"")
    time.sleep(1)
    print("Your confidence startles the dragon, catching him off guard.")
    time.sleep(1)
    print("While the dragon is startled you look around yourself.")
    time.sleep(1)
    print("You see 3 weapons lying scattered around.")
    time.sleep(1)
    print("You see a wand one meter away from you, an iron sword 10 meters away from you, and a longbow 50 meters away from you.")
    time.sleep(1)

    choice = input("Which weapon do you pick up [1] the wand, [2] the iron sword, or [3] the longbow? ")

    if choice == "1":
        print("You quickly pick up the wand, but you have a problem.")
        time.sleep(1)
        print("You don't know any magic.")
        time.sleep(1)
        print("The dragon laughs and quickly kills you.")
        time.sleep(1)
        player.hp -= 100

    elif choice == "2":
        print("You run over to the iron sword, pick it up, and run fast towards the dragon.")
        time.sleep(1)
        print("The dragon does not even have time to get his guard up before you slash his throat.")
        time.sleep(1)
        return tenth_challenge()

    elif choice == "3":
        print("You run to the longbow, but it takes some time.")
        time.sleep(1)
        print("The dragon files faster than you could ever run, he is only 10 meters away and you stress trying to fire the longbow, but you dont have enough time.")
        time.sleep(1)
        print("The dragon is too close.")
        time.sleep(1)
        print("You get brutally murdered by the dragon.")
        time.sleep(1)
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return ninth_challenge()


def tenth_challenge():
    print("The dragon drops to the ground with a BANG.")
    time.sleep(1)
    print("You try to roll the dragon away, to get to the food.")
    time.sleep(1)
    print("You manage to roll him over, and you see something shiny sticking out from his throat where you had slashed him.")
    time.sleep(1)
    print("Out of curiosity for what this item could be, you take the shiny object out of his throat and see that it is completely clean.")
    time.sleep(1)
    print("It is a crystal.")
    time.sleep(1)
    print(f"Good job {player.name}, you have found the Neuron Crystal.")
    time.sleep(1)
    print("You take the food back to the Old man.")
    time.sleep(1)
    print("\"Thank you so much for the help, but I must ask, did you kill the dragon?\" The Old man asks.")
    time.sleep(1)

    choice = input("[1] \"Yes, it was no problem at all.\" or [2] \"Why do you ask?\" ")

    if choice == "1":
        print("\"Did you find the Crystal in it's neck?\" The Old man asks, suddenly not looking that old anymore.")
        time.sleep(1)
        return eleventh_challenge()

    elif choice == "2":
        print("\"No reason at all, did you kill the dragon?\", the Old man yells!")
        time.sleep(1)
        print("As he was yelling louder and louder about if you killed the dragon, he stops looking like an Old man.")
        time.sleep(1)
        print(f"\"Who are you?\" {player.name} asks.")
        time.sleep(1)
        print("\"I am the only person who has ever been able to survive on this world, I am the all powerful Sorcerer\", the Sorcerer yells out.")
        time.sleep(1)
        print("As the Sorcerer yells out the last words, he casts a spell that shatters your body into many pieces.")
        time.sleep(1)
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return tenth_challenge()


def eleventh_challenge():
    print("You start walking slowly backwards and away from the person who was an Old man.")
    time.sleep(1)
    print("Who are you? You ask while still backing away.")
    time.sleep(1)
    print("\"I am the Sorcerer who has been the only person to ever survive this world!\" the Sorcerer says with a mighty voice.")
    time.sleep(1)
    print("\"GIVE ME THE CRYSTAL NOW!!!\" The Sorcerer says calmly.")
    time.sleep(1)

    choice = input("[1] Make a run for it, [2] fight the Sorcerer or [3] give him the Neuron Crystal. ")

    if choice == "1":
        print("You turn your back towards the Sorcerer and run for your life!")
        time.sleep(1)
        print("The startled Sorcerer is stunned, giving you a head start.")
        time.sleep(1)
        return twelfth_challenge()

    elif choice == "2":
        print("You raise your guard, ready to attack the Sorcerer.")
        time.sleep(1)
        print("Before you know it you are dead from his magic.")
        time.sleep()

    elif choice == "3":
        print("You hand him the Neuron Crystal")
        time.sleep(1)
        print(f"\"Thank you for your help {player.name}, but I do not require your services any more, \" the Sorcerer says.")
        print("The Sorcerer stabs your as you help him.")
        time.sleep(1)

    else:
        print("Invalid input, please check your spelling and try again.")
        return eleventh_challenge()


def twelfth_challenge():
    print("You run in the opposite direction from the Sorcerer and you spot 3 portals in the distance.")
    time.sleep(1)
    print("You are closing in on the portals and see that one of them is closer to you than the others.")
    time.sleep(1)
    print("The Sorcerer is catching up, which portal do you want to go to?")
    time.sleep(1)
    choice = input("[1] The closest portal or [2] one of the portals further back. ")

    if choice == "1":
        print("You are running as fast as possible to reach the portal before the Sorcerer catches up to you.")
        print("The Sorcerer is slowly, but steadily catching up to you.")
        print("You are closing in on the portal...")
        print("The portal gets closer and closer, but so do the Sorcerer.")
        print("...")
        print("And...")
        print("You reach the portal barely in time before the Sorcerer catches up to you.")

    elif choice == "2":
        print("You are running as fast as possible to reach the portal before the Sorcerer catches up to you.")
        print("The Sorcerer is slowly, but steadily catching up to you.")
        print("You are still far away from the portals, but the Sorcerer is catching up.")
        print("The Sorcerer catches up to you and kills you with some dark magic.")
        player.hp -= 100

    else:
        print("Invalid input, please check your spelling and try again.")
        return twelfth_challenge()"""