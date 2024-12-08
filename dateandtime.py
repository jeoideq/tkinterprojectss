import tkinter
import time 
import datetime

screen=tkinter.Tk()
screen.geometry("400x200")
screen.title("Date and Time")

label1=tkinter.Label(screen, bg="blue", fg="white", width=35, height=5)
label1.pack()

label2=tkinter.Label(screen, bg="blue", fg="white", width=35, height=5)
label2.pack()


def date():
    datevariable=datetime.datetime.now().strftime("%A: %B: %d: %Y")
    label1.config(text=datevariable)
    label1.after(1000, date)
date()

def clock():
    timevariable=time.strftime("%H:%M:%S")
    label2.config(text=timevariable)
    label2.after(1000,clock)
clock()



screen.mainloop()