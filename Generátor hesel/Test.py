from tkinter import *
import random


#Okno
screen = Tk()
screen.minsize(400,300)
screen.title("Generátor hesel")
screen.resizable(False, False)

#Proměnné
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "ch", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
caps_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "CH", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_chars = ["/", "?", "!", "#", "*", "@", "&", "{"]
password = []



#Funkce

def letters_open():
    if letters_checkbox.get() == 1:
        number_letters.config(state="normal")
    else:
        number_letters.config(state="disabled")

def numbers_open():
    if numbers_checkbox.get() == 1:
        number_numbers.config(state="normal")
    else:
        number_numbers.config(state="disabled")

def chars_open():
    if chars_checkbox.get() == 1:
        number_chars.config(state="normal")
    else:
        number_chars.config(state="disabled")

def caps_open():
    if caps_checkbox.get() == 1:
        number_caps_letters.config(state="normal")
    else:
        number_caps_letters.config(state="disabled")



def adding_password():
    password.clear()
    result.config(text="")
    try:
        #Naskládání znaků
        if letters_checkbox.get()==1:
            let = number_letters.get()
            let_int = int(let)
            for one_letter in range(0, let_int):
                password.append(letters[random.randint(0, len(letters) - 1)])
        else:
            let = 0
            for one_letter in range(0, let):
                password.append(letters[random.randint(0, len(letters) - 1)])

        if numbers_checkbox.get() == 1:
            num = number_numbers.get()
            num_int = int(num)
            for one_number in range(0, num_int):
                password.append(numbers[random.randint(0, len(numbers) - 1)])
        else:
            num = 0
            for one_number in range(0, num):
                password.append(numbers[random.randint(0, len(numbers) - 1)])

        if chars_checkbox.get() == 1:
            char = number_chars.get()
            char_int = int(char)
            for one_number in range(0, char_int):
                password.append(special_chars[random.randint(0, len(special_chars) - 1)])
        else:
            char = 0
            for one_number in range(0, char):
                password.append(special_chars[random.randint(0, len(special_chars) - 1)])

        if caps_checkbox.get() == 1:
            caps = number_caps_letters.get()
            caps_int = int(caps)
            for one_cap in range(0, caps_int):
                password.append(caps_letters[random.randint(0, len(caps_letters)-1)])
        else:
            caps = 0
            for one_cap in range (0, caps):
                password.append(caps_letters[random.randint(0, len(caps_letters)-1)])

        #Zamíchání hesla
        random.shuffle(password)

        #Převod na string heslo
        password_str = ""
        for one_x in password:
            password_str += str(one_x)

        result.config(text=f"Vaše nové heslo je:\n {password_str}")
        button ["text"] = "Znovu vygenerovat heslo"


    except:
        result.config(text="CHYBA: musíte zvolit počet znaků")


#Framy
input_frame = Frame(screen)
input_frame.pack()

#Inputy
number_letters = Entry(input_frame, width=5)
number_letters.grid(row=0, column=1)
number_letters.config(state="disabled")

number_numbers = Entry(input_frame,width=5)
number_numbers.grid(row=1, column=1)
number_numbers.config(state="disabled")

number_chars = Entry(input_frame,width=5)
number_chars.grid(row=2, column=1)
number_chars.config(state="disabled")

number_caps_letters = Entry(input_frame, width=5)
number_caps_letters.grid(row=3, column=1)
number_caps_letters.config(state="disabled")




#Checkbox
letters_checkbox = IntVar()
check_letters = Checkbutton(input_frame, text="Chci přidat písmena", variable=letters_checkbox, command=letters_open)
check_letters.grid(row=0, column=0)

numbers_checkbox = IntVar()
check_numbers = Checkbutton(input_frame, text="Chci přidat čísla", variable=numbers_checkbox, command=numbers_open)
check_numbers.grid(row=1, column=0)

chars_checkbox = IntVar()
check_chars = Checkbutton(input_frame, text="Chci přidat spec. znaky", variable=chars_checkbox, command=chars_open)
check_chars.grid(row=2, column=0)

caps_checkbox = IntVar()
check_caps_letters  = Checkbutton(input_frame, text="Chci přidat velká písmena", variable=caps_checkbox, command=caps_open)
check_caps_letters.grid(row=3, column=0)

#Tlačítko
#button_img = PhotoImage(file="generator hesel.png")
button = Button(text="Vygenerovat heslo", command=adding_password, font=("Arial", 13))
button.pack(pady=30)
button.config()

#Label
result = Label(text="Vaše nové heslo je: ", font=("Arial", 15, "bold"))
result.pack()
result.config(wraplength=200)
letter_label = Label(input_frame, text="Zadejte počet písmen")
letter_label.grid(row=0, column=2)

number_label = Label(input_frame, text="Zadejte počet čísel")
number_label.grid(row=1, column=2)

char_label = Label(input_frame, text="Zadejte počet znaků")
char_label.grid(row=2, column=2)

caps_letters_label = Label(input_frame, text="Zadejte počet velkých písmen")
caps_letters_label.grid(row=3, column=2)







#Hlavní cyklus
screen.mainloop()


