from tkinter import *
import random



#Okno
screen = Tk()
screen.minsize(400,300)
screen.title("Generátor hesel")
screen.resizable(False, False)

#Proměnné
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "ch", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["/", "?", "!", "#", "*", "@", "&", "{"]
password = []



#Funkce

def adding_letters():
    if letters_checkbox.get() == 1:
        let = number_letters.get()
        let_int = int(let)
        for one_letter in range(0, let_int):
            password.append(letters[random.randint(0, len(letters) - 1)])

    if letters_checkbox.get() == 0:
        let = number_letters.get()
        let_int = int(let)
        for one_letter in range(0, let_int):
            password.append("")


    if numbers_checkbox.get() == 1:
        num = number_numbers.get()
        num_int = int(num)
        for one_number in range(0, num_int):
            password.append(numbers[random.randint(0, len(numbers) - 1)])
    else:
        password.append()

    if chars_checkbox.get() == 1:
        char = number_chars.get()
        char_int = int(char)
        for one_number in range(0, char_int):
            password.append(special_chars[random.randint(0, len(special_chars) - 1)])
    else:
        password.append()

    print(password)



#Framy
input_frame = Frame(screen)
input_frame.pack()



#Inputy
number_letters = Entry(input_frame,text ="Kolik chcete písmen: ")
number_letters.grid(row=0, column=1)

number_numbers = Entry(input_frame, text = "Kolik chcete čísel: ")
number_numbers.grid(row=1, column=1)

number_chars = Entry(input_frame,text = "Kolik chcete znaků: ")
number_chars.grid(row=2, column=1)


#Checkbox
letters_checkbox = IntVar()
check_letters = Checkbutton(input_frame, text="Chci přidat písmena", variable=letters_checkbox)
check_letters.grid(row=0, column=0)

numbers_checkbox = IntVar()
check_numbers = Checkbutton(input_frame, text="Chci přidat čísla", variable=numbers_checkbox)
check_numbers.grid(row=1, column=0)

chars_checkbox = IntVar()
check_chars = Checkbutton(input_frame, text="Chci přidat spec. znaky", variable=chars_checkbox)
check_chars.grid(row=2, column=0)

#Tlačítko
button = Button(text="zkus", command=adding_letters)
button.pack()

#Label
result = Label(text="0")
result.pack()






#Hlavní cyklus
screen.mainloop()


