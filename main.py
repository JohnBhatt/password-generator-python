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
randomsym =""
randomnum =""
randomletter = ""
for sym_count in range (0, nr_symbols):
  randomsym += random.choice(symbols)
for num_count in range (0, nr_numbers):
  randomnum += random.choice(numbers)
for let_count in range  (0,nr_letters):
  randomletter += random.choice(letters)

pass_new = randomnum + randomsym + randomletter

print(f"Secure Password will be :   {pass_new}")

print()
#randomsym = random.choice(symbols)
#print(randomsym)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list =[]

for sym_count in range (0, nr_symbols):
  password_list += random.choice(symbols)
for num_count in range (0, nr_numbers):
  password_list += random.choice(numbers)
for let_count in range  (0,nr_letters):
  password_list += random.choice(letters)

random.shuffle(password_list)
finalPass = ""
for char in password_list:
  finalPass += char

print(f"Your more secure password is : {finalPass}") 
