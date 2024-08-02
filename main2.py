# hard level to to generator python passsword

import random as r

letters = ['a','b','c','d', 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']

numbers = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0']

symbols = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '+' , '.']

ln_letters = int(input("How many letter would you like in your password?\n"))
ln_numbers = int(input("How many numbers would you like in your password?\n"))
ln_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []

for char in range(1,ln_letters +1 ):
    random_num = r.randint(0,len(letters)-1)
    password_list.append(letters[random_num])

for sym in range(1,ln_symbols +1 ):
    random_num = r.choice(symbols)
    password_list.append(random_num)

for num in range(1,ln_numbers +1 ):
    random_num = r.choice(numbers)
    password_list.append(random_num)


# print(password_list)

# shuffle(list_name) is a reorder the element
r.shuffle(password_list)
# print(password_list)
password =""

for passw in range(0, len(password_list)):
    password += password_list[passw]

print(f"Here is your password: {password}")