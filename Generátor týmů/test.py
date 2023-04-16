from tkinter import *




screen = Tk()
screen.minsize(200, 200)

def subject_a():
    screen_A = Tk()
    screen_A.minsize(200, 200)

    label_a = Label(screen_A, text="jslkfjdlkfjlksdjflkf", font=("Arial", 15, "bold"))
    label_a.grid(row=0, column=0)

    screen_A.mainloop()



def subject_b():
    screen_B = Tk()
    screen_B.minsize(200, 200)

    label_b = Label(screen_B, text="peowpquepoweiqpwre", font=("Arial", 12))
    label_b.grid(row=0, column=0)
    screen.quit()
    screen_B.mainloop()


button_A = Button(text="A", command=subject_a)
button_A.grid(row=0, column=0, padx=20)

button_B = Button(text="B", command=subject_b)
button_B.grid(row=0, column=1, padx=20)






screen.mainloop()