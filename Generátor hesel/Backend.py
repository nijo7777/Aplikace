import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "ch", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["/", "?", "!", "#", "*", "@", "&", "{"]


password =[]


number_letters = int(input("Kolik chcete písmen: "))
number_numbers = int(input("Kolik chcete čísel: "))
number_chars = int(input("Kolik chcete znaků: "))


for one_letter in range(0, number_letters):
    password.append(letters[random.randint(0, len(letters)-1)])

for one_number in range(0, number_numbers):
    password.append(numbers[random.randint(0, len(numbers)-1)])

for one_char in range(0, number_chars):
    password.append(special_chars[random.randint(0, len(special_chars)-1)])

random.shuffle(password)


password_str = ""

for one_x in password:
    password_str += one_x


print(password_str)