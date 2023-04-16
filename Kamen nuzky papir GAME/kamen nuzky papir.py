import random
from tkinter import *

#Okno
screen = Tk()
screen.title("Kámen nůžky papír | hra")
screen.minsize(500, 500)
screen.resizable(True, True)

#Proměnné
main_font = ("Arial", 18, "bold")
enemy_choice_options = ["kámen", "nůžky", "papír"]

#Funkce
def player_choice():
    player_option = player_result ["text"] = player_input.get().lower()
    enemy_option = enemy_result ["text"] = random.choice(enemy_choice_options)
    player_input.delete(0, END)

    if player_option == "kámen" and enemy_option == "kámen":
        result_text.config(text="Remíza")
    elif player_option == "kámen" and enemy_option == "nůžky":
        result_text.config(text=" Kámen tupí nůžky | Výhrál si")
    elif player_option == "kámen" and enemy_option == "papír":
        result_text.config(text="Papír balí kámen | Prohrál si")
    elif player_option == "nůžky" and enemy_option == "kámen":
        result_text.config(text="Kámen tupí nůžky | prohrál si")
    elif player_option == "nůžky" and enemy_option == "nůžky":
        result_text.config(text="Remíza")
    elif player_option == "nůžky" and enemy_option == "papír":
        result_text.config(text="Nůžky stříhají kámen | Vyhrál si")
    elif player_option == "papír" and enemy_option == "kámen":
        result_text.config(text="Papír balí kámen | Vyhrál si")
    elif player_option == "papír" and enemy_option == "nůžky":
        result_text.config(text="Nůžky stříhají kámen | Prohrál si")
    elif player_option == "papír" and enemy_option == "papír":
        result_text.config(text="Remíza")


#Labels
#Hráč
player_result_title = Label(text="HRÁČ HRAJE:", font=main_font)
player_result_title.grid(row=0, column=1, pady=20, padx=10)

player_result = Label(text="", font=("Arial", 12))
player_result.grid(row=1, column=1, pady=10, padx=10)

enemy_result_title = Label(text="SOUPEŘ HRÁL:", font=main_font)
enemy_result_title.grid(row=0, column=0, pady=20, padx=10)

enemy_result = Label(text="", font=("Arial", 12))
enemy_result.grid(row=1, column=0, pady=10, padx=10)

result_label = Label(text="Výsledek je: ", font=main_font)
result_label.grid(row=3, column=0, pady=(50, 0))


result_text = Label(text="", font=("Arial", 13, "bold"))
result_text.grid(row=3, column=1, pady=(50, 0))

#Input
player_input = Entry(font=main_font, width=10)
player_input.grid(row=2, column=0, pady=(50, 0))
player_input.focus()

#Tlačítko
button = Button(text="HRAJEM", font=main_font, command=player_choice)
button.grid(row=2, column=1, pady=(50, 0))
screen.bind("<Return>", lambda event: button.invoke())


#Hlavní cyklus
screen.mainloop()