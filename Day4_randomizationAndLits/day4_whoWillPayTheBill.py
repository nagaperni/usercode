"""
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
"""

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
random_choice = random.randint(0, len(names) - 1)

person_paying = names[random_choice]

print(f"{person_paying} will pay the bill!")


