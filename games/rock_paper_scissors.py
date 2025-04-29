import random
play = ["Rock", "Paper", "Scissors"]
computer = play[random.randint(0,2)]
player = False

while player == False:
    player = input("Rock, Paper or Scissors? ")

    if player == computer:
        print("It's a tie!")

    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose! {computer} covers {player}")
        else:
            print(f"You win! {player} smashes {computer}")

    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lose! {computer} cuts {player}")
        else:
            print(f"You win! {player} covers {computer}")

    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lose! {computer} smashes {player}")
        else:
            print(f"You win! {player} cuts {computer}")

    else:
        print("That is not a valid play. Check the spelling!")

player = False
computer = play[random.randint(0,2)]

