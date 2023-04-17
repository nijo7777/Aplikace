import tkinter
from tkinter import *
import random


#Okno
screen = Tk()
screen.title("Generátor týmů")
screen.minsize(700, 700)

#Funkce
def generate_team():
    value = scale_meter.get()
    if value == 5:
        random_index_1 = random.randint(0, len(team_list_5_star) - 1)
        random_index_2 = random.randint(0, len(team_list_5_star) - 1)
        random_team_1 = team_list_5_star[random_index_1]
        random_team_1_img = team_list_img_5_star[random_index_1]
        random_team_2 = team_list_5_star[random_index_2]
        random_team_2_img = team_list_img_5_star[random_index_2]
    elif value == 4:
        random_index_1 = random.randint(0, len(team_list_4_star) - 1)
        random_index_2 = random.randint(0, len(team_list_4_star) - 1)
        random_team_1 = team_list_4_star[random_index_1]
        random_team_1_img = team_list_img_4_star[random_index_1]
        random_team_2 = team_list_4_star[random_index_2]
        random_team_2_img = team_list_img_4_star[random_index_2]
    team_1.config(text=random_team_1)
    team_2.config(text=random_team_2)
    team_1_img_label.config(image=random_team_1_img)
    team_2_img_label.config(image=random_team_2_img)
    return


#Obrázky
barcelona_img = PhotoImage(file="Images/barcelona 1.png")
real_img = PhotoImage(file="Images/real madrid 1.png")
bayern_img = PhotoImage(file="Images/bayern 1.png")
chelsea_img = PhotoImage(file="Images/chelsea 1.png")
liberpool_img = PhotoImage(file="Images/liverpool 1.png")

#Proměnné

global team_list_5_star
team_list_5_star = ["FC Barcelona", "Real Madrid", "Bayern Mnichov", "Chelsea FC", "Liverpool"]
global team_list_img_5_star 
team_list_img_5_star = [barcelona_img, real_img, bayern_img, chelsea_img, liberpool_img]

global team_list_4_star 
team_list_4_star= ["Arsenal", "Spurs", "United", "Atletico", "Neapol"]
global team_list_img_4_star 
team_list_img_4_star = [barcelona_img, real_img, bayern_img, chelsea_img, liberpool_img]


index_left_team = 0
index_right_team = 1

#Labels
team_1 = Label(text=team_list_5_star[index_left_team], font=("Arial", 20, "bold"))
team_1.grid(row=0, column=0, padx=20, pady=20)

team_2 = Label(text=team_list_5_star[index_right_team], font=("Arial", 20, "bold"))
team_2.grid(row=0, column=2, padx=20, pady=20)

vs_label = Label(text="VS.", font=("Arial", 25, "bold"))
vs_label.grid(row=1, column=1)

#Labels obrázky
team_1_img_label = Label(image=team_list_img_5_star[index_left_team])
team_1_img_label.grid(row=1, column=0, padx=20, pady=20)

team_2_img_label = Label(image=team_list_img_5_star[index_right_team])
team_2_img_label.grid(row=1, column=2, padx=20, pady=20)

#Tlačítko
button = Button(text="Vygenerovat týmy", command=generate_team)
button.grid(row=2, column=1)

#Posuvník
scale_meter = Scale(from_=0, to=5, orient=HORIZONTAL, tickinterval=0.5, length=250)
scale_meter.grid(row=3, column=1)


#Hlavní cyklus
screen.mainloop()