#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
eazy_pw = ''
for x in range(1,nr_letters + 1):
    random_letter = random.randint(0,len(letters)-1) #(-1) to pass the right slice
    print(random_letter)
    eazy_pw += letters[random_letter]

for x in range(0,nr_symbols):
    random_symbol = random.randint(0,len(symbols)-1)
    print(random_symbol)
    eazy_pw += symbols[random_symbol]

for x in range(0,nr_numbers):
    random_number = random.randint(0,len(numbers)-1)
    print(random_number)
    eazy_pw += numbers[random_number]

print(eazy_pw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pw = []
for x in range(1,nr_letters + 1):
    random_letter = random.randint(0,len(letters)-1)
    hard_pw += letters[random_letter]

for x in range(0,nr_symbols):
    random_symbol = random.randint(0,len(symbols)-1)
    hard_pw += symbols[random_symbol]

for x in range(0,nr_numbers):
    random_number = random.randint(0,len(numbers)-1)
    hard_pw += numbers[random_number]

random.shuffle(hard_pw)

password = ''
for char in hard_pw:
    password += char

print(password)