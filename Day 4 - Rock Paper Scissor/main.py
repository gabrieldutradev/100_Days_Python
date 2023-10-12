rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

import random
player = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if player > 2 or player < 0:
    print("You type an invalid number!")
else:
    print(f"You choose {player}.")
    print(game_images[player])

    computer = int(random.randint(0 , 2))
    print(f"Computer choose {computer}.")
    print(game_images[computer])

    if player == 0:
        if computer == 0:
            print("DRAW!")
        elif computer == 1:
            print("You Lose!")
        else:
            print("You Win!")
    elif player == 1:
        if computer == 0:
            print("You Win!")
        elif computer == 1:
            print("DRAW!")
        else:
            print("You Lose!")
    elif player == 2:
        if computer == 0:
            print("You Lose!")
        elif computer == 1:
            print("You Win!")
        else:
            print("DRAW!")