import tkinter
import time

screen=tkinter.Tk()
screen.geometry("400x100")
screen.title("Clock")

label=tkinter.Label(screen, bg="orange", fg="white", width=35, height=5)
label.pack()

def clock():
    timevariable=time.strftime("%H:%M:%S")
    label.config(text=timevariable)
    label.after(1000, clock)
clock()









screen.mainloop()