from tkinter import *
import math
from tkinter import messagebox

#Okno
screen = Tk()
screen.minsize(height=500, width=330)
screen.title("Kalkulačka")
result_frame = Frame(screen)

def num_1():
    global a
    a = result.insert(END, int(button_1["text"]))

def num_2():
    global b
    b = result.insert(END, int(button_2["text"]))

def plus_function():
    global num3
    num3 = result.insert(END, button_plus["text"])

def result_function():
    num_result = a + b
    result.insert(num_result)

#Framy
result_frame.pack()

calculator_frame = Frame(screen)
calculator_frame.pack()


#Result frame obsah
result = Entry(result_frame,  width=17, borderwidth=2, bg="red", font=("Arial", 20))
result.pack(pady=20)
result.focus()


#Tlačítka
    #Proměnné tlačítka
width = 8
height = 4
background_color_light = "darkgrey"
background_color_dark = "grey"

button_C = Button(calculator_frame, text="C", width=width, height=height, bg=background_color_dark, command=result_function)
button_C.grid(row=0, column=0)

button_odm = Button(calculator_frame, text="odm.", width=width, height=height, bg=background_color_dark)
button_odm.grid(row=0, column=1)

button_moc = Button(calculator_frame, text="moc.", width=width, height=height, bg=background_color_dark)
button_moc.grid(row=0, column=2)

button_proc = Button(calculator_frame, text="%", width=width, height=height, bg=background_color_dark)
button_proc.grid(row=0, column=3)

button_1 = Button(calculator_frame, text="1", width=width, height=height, bg=background_color_light, command=num_1)
button_1.grid(row=1, column=0)

button_2 = Button(calculator_frame, text="2", width=width, height=height, bg=background_color_light, command=num_2)
button_2.grid(row=1, column=1)

button_3 = Button(calculator_frame, text="3", width=width, height=height, bg=background_color_light)
button_3.grid(row=1, column=2)

button_plus = Button(calculator_frame, text="+", width=width, height=height, bg=background_color_dark)
button_plus.grid(row=1, column=3)

button_4 = Button(calculator_frame, text="4", width=width, height=height, bg=background_color_light)
button_4.grid(row=2, column=0)

button_5 = Button(calculator_frame, text="5", width=width, height=height, bg=background_color_light)
button_5.grid(row=2, column=1)

button_6 = Button(calculator_frame, text="6", width=width, height=height, bg=background_color_light)
button_6.grid(row=2, column=2)

button_minus = Button(calculator_frame, text="-", width=width, height=height, bg=background_color_dark)
button_minus.grid(row=2, column=3)

button_7 = Button(calculator_frame, text="7", width=width, height=height, bg=background_color_light)
button_7.grid(row=3, column=0)

button_8 = Button(calculator_frame, text="8", width=width, height=height, bg=background_color_light)
button_8.grid(row=3, column=1)

button_9 = Button(calculator_frame, text="9", width=width, height=height, bg=background_color_light)
button_9.grid(row=3, column=2)

button_krat = Button(calculator_frame, text="*", width=width, height=height, bg=background_color_dark)
button_krat.grid(row=3, column=3)

button_0 = Button(calculator_frame, text="0", width=width, height=height, bg=background_color_light)
button_0.grid(row=4, column=0)

button_tecka = Button(calculator_frame, text=".", width=width, height=height, bg=background_color_light)
button_tecka.grid(row=4, column=1)

button_rovno = Button(calculator_frame, text="=", width=width, height=height, bg="orange")
button_rovno.grid(row=4, column=2)

button_deleno = Button(calculator_frame, text="/", width=width, height=height, bg=background_color_dark)
button_deleno.grid(row=4, column=3)

#Hlavní cyklus
screen.mainloop()