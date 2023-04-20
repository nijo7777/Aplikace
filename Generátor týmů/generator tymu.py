from tkinter import *
import random
from PIL import ImageTk, Image
from tkinter import ttk
import team_lists

#Okno
screen = Tk()
screen.title("Generátor týmů")
screen.minsize(700, 700)

#Funkce
def rating(selected_league):
    league = variable.get()
    if league == "Anglie":
        min_scale_meter.config(from_=3.5, to=5)
    elif league == "Španělsko":
        min_scale_meter.config(from_=3.5, to=5)
    elif league == "Itálie":
        min_scale_meter.config(from_=3.5, to=5)
    elif league == "Německo":
        min_scale_meter.config(from_=3.5, to=5)
    elif league == "Francie":
        min_scale_meter.config(from_=3, to=5)


    if league == "Anglie":
        max_scale_meter.config(from_=3.5, to=5)
    elif league == "Španělsko":
        max_scale_meter.config(from_=3.5, to=5)
    elif league == "Itálie":
        max_scale_meter.config(from_=3.5, to=5)
    elif league == "Německo":
        max_scale_meter.config(from_=3.5, to=5)
    elif league == "Francie":
        max_scale_meter.config(from_=3, to=5)



def generate_team():
    max_value = max_scale_meter.get()
    min_value = min_scale_meter.get()
    league = variable.get()
    if league == "Anglie" and min_value == 5 and max_value == 5:
        random_index_1 = random.randint(0, len(team_lists.england_list_5_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_5_star) - 1)
        random_team_1 = team_lists.england_list_5_star[random_index_1]
        random_team_2 = team_lists.england_list_5_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 4.5 and max_value == 5:
        random_index_1 = random.randint(0, len(team_lists.england_list_4half_to_5_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_4half_to_5_star) - 1)
        random_team_1 = team_lists.england_list_4half_to_5_star[random_index_1]
        random_team_2 = team_lists.england_list_4half_to_5_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 4 and max_value == 5:
        random_index_1 = random.randint(0, len(team_lists.england_list_4_to_5_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_4_to_5_star) - 1)
        random_team_1 = team_lists.england_list_4_to_5_star[random_index_1]
        random_team_2 = team_lists.england_list_4_to_5_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 3.5 and max_value == 5:
        random_index_1 = random.randint(0, len(team_lists.england_list_3half_to_5_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_3half_to_5_star) - 1)
        random_team_1 = team_lists.england_list_3half_to_5_star[random_index_1]
        random_team_2 = team_lists.england_list_3half_to_5_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 4.5 and max_value == 4.5:
        random_index_1 = random.randint(0, len(team_lists.england_list_4half_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_4half_star) - 1)
        random_team_1 = team_lists.england_list_4half_star[random_index_1]
        random_team_2 = team_lists.england_list_4half_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 4 and max_value == 4.5:
        random_index_1 = random.randint(0, len(team_lists.england_list_4_to_4half_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_4_to_4half_star) - 1)
        random_team_1 = team_lists.england_list_4_to_4half_star[random_index_1]
        random_team_2 = team_lists.england_list_4_to_4half_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 3.5 and max_value == 4.5:
        random_index_1 = random.randint(0, len(team_lists.england_list_3half_to_4half_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_3half_to_4half_star) - 1)
        random_team_1 = team_lists.england_list_3half_to_4half_star[random_index_1]
        random_team_2 = team_lists.england_list_3half_to_4half_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 4 and max_value == 4:
        random_index_1 = random.randint(0, len(team_lists.england_list_4_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_4_star) - 1)
        random_team_1 = team_lists.england_list_4_star[random_index_1]
        random_team_2 = team_lists.england_list_4_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 3.5 and max_value == 4:
        random_index_1 = random.randint(0, len(team_lists.england_list_3half_to_4_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_3half_to_4_star) - 1)
        random_team_1 = team_lists.england_list_3half_to_4_star[random_index_1]
        random_team_2 = team_lists.england_list_3half_to_4_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)
    elif league == "Anglie" and min_value == 3.5 and max_value == 3.5:
        random_index_1 = random.randint(0, len(team_lists.england_list_3half_star) - 1)
        random_index_2 = random.randint(0, len(team_lists.england_list_3half_star) - 1)
        random_team_1 = team_lists.england_list_3half_star[random_index_1]
        random_team_2 = team_lists.england_list_3half_star[random_index_2]
        team_1.config(text=random_team_1)
        team_2.config(text=random_team_2)

    return


#Obrázky resize

arsenal_imgage = Image.open("Images/arsenal 1.png")
arsenal_imgage = arsenal_imgage.resize((250, 200))

barca_imgage = Image.open("Images/barcelona 1.png")
barca_imgage = barca_imgage.resize((250, 200))

bayern_imgage = Image.open("Images/bayern 1.png")
bayern_imgage = bayern_imgage.resize((250, 200))

city_imgage = Image.open("Images/city 1.png")
city_imgage = city_imgage.resize((250, 200))

chelsea_imgage = Image.open("Images/chelsea 1.png")
chelsea_imgage = chelsea_imgage.resize((250, 200))

liverpool_imgage = Image.open("Images/liverpool 1.png")
liverpool_imgage = liverpool_imgage.resize((250, 200))

real_imgage = Image.open("Images/real madrid 1.png")
real_imgage = real_imgage.resize((250, 200))

united_image = Image.open("Images/united 1.png")
united_image = united_image.resize((250, 200))

westham_image = Image.open("Images/west ham 1.png")
westham_image = westham_image.resize((250, 200))

everton_image = Image.open("Images/everton 1.png")
everton_image = everton_image.resize((250, 200))

lester_image = Image.open("Images/lester 1.png")
lester_image = lester_image.resize((250, 200))

newcastle_image = Image.open("Images/newcastle 1.png")
newcastle_image = newcastle_image.resize((250, 200))

spurs_image = Image.open("Images/spurs 1.png")
spurs_image = spurs_image.resize((250, 200))





#Obrázky 5 star

barcelona_img = ImageTk.PhotoImage(barca_imgage)
real_img = ImageTk.PhotoImage(real_imgage)
bayern_img = ImageTk.PhotoImage(bayern_imgage)
city_img = ImageTk.PhotoImage(city_imgage)
liverpool_img = ImageTk.PhotoImage(liverpool_imgage)

#Obrázky 4 star

chelsea_img = ImageTk.PhotoImage(chelsea_imgage)
united_img = ImageTk.PhotoImage(united_image)
spurs_img = ImageTk.PhotoImage(spurs_image)
everton_img = ImageTk.PhotoImage(everton_image)
arsenal_img = ImageTk.PhotoImage(arsenal_imgage)

#Obrázky 3 star

lester_img = ImageTk.PhotoImage(lester_image)
westham_img = ImageTk.PhotoImage(westham_image)
newcastle_img = ImageTk.PhotoImage(newcastle_image)


#Seznamy

team_list_5_star = ["FC Barcelona", "Real Madrid", "Bayern Mnichov", "Manchester", "Liverpool"]
team_list_img_5_star = [barcelona_img, real_img, bayern_img, city_img, liverpool_img]

team_list_4_star = ["Chelsea", "United", "Spurs", "Everton", "Arsenal"]
team_list_img_4_star = [chelsea_img, united_img, spurs_img, everton_img, arsenal_img]

team_list_3_star = ["Leicester FC", "West Ham", "FC Newcastle"]
team_list_img_3_star = [lester_img, westham_img, newcastle_img]


index_left_team = 0
index_right_team = 1


#Labels
team_1 = Label(text=team_list_5_star[index_left_team], font=("Arial", 20, "bold"))
team_1.grid(row=0, column=0, padx=20, pady=20)

team_2 = Label(text=team_list_5_star[index_right_team], font=("Arial", 20, "bold"))
team_2.grid(row=0, column=2, padx=20, pady=20)

vs_label = Label(text="VS.", font=("Arial", 25, "bold"))
vs_label.grid(row=1, column=1)

min_level_label = Label(text="Zvolte minimální počet hvězd", font=("Arial", 15))
min_level_label.grid(row=3, column=0)

max_level_label = Label(text="Zvolte maximální počet hvězd", font=("Arial", 15))
max_level_label.grid(row=3, column=2)

#Labels obrázky
team_1_img_label = Label(image=team_list_img_5_star[index_left_team])
team_1_img_label.grid(row=1, column=0, padx=20, pady=20)

team_2_img_label = Label(image=team_list_img_5_star[index_right_team])
team_2_img_label.grid(row=1, column=2, padx=20, pady=20)

#Tlačítko

button_img = PhotoImage(file="Images/Tlačítko.png")
button = Button(text="Vygenerovat týmy", command=generate_team, image=button_img, borderwidth=0)
button.grid(row=2, column=1, padx=50, pady=35)

#Posuvník

min_scale_meter = Scale(from_=3.5, to=5, orient=HORIZONTAL, resolution=0.5, length=250, sliderrelief=FLAT)
min_scale_meter.grid(row=4, column=0)

max_scale_meter = Scale(from_=3.5, to=5, orient=HORIZONTAL, resolution=0.5, length=250)
max_scale_meter.grid(row=4, column=2)

#Výběr ligy
leagues = ["Anglie", "Španělsko", "Německo", "Itálie", "Francie"]

variable = StringVar()
variable.set(leagues[0])
dropdown = OptionMenu(screen, variable, *leagues, command=rating)
dropdown.grid(row=5, column=0, pady=20, padx=10)
dropdown.config(font=("Arial", 15))



#Hlavní cyklus
screen.mainloop()