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

#Write your code below this line 👇
"""
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""
### User choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Please choice from the given numbers.")

### Computer choice
print("Computer chose:")
import random
computer_choice  = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

### Who wins logic
if computer_choice == user_choice:
    print("It's a draw")
elif computer_choice == 0:
    if user_choice == 1:
        print("You win")
    else:
        print("You lose")
elif computer_choice == 1:
    if user_choice == 2:
        print("You win")
    else:
        print("You lose")
elif computer_choice == 2:
    if user_choice == 0:
        print("You win")
    else:
        print("You lose")