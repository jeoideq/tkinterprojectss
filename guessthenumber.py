import tkinter
import random
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("800x400")
screen.title("Guess The Number Game")

correct_num=random.randint(1,10)

def guess_the_number():
    guess_num = int(entry2.get())
    if guess_num < correct_num:
        tkinter.messagebox.askyesno("Guess the number", "the number is higher")
    elif guess_num > correct_num:
        tkinter.messagebox.showinfo("Guess the number", "the number is lower")
    else:
        tkinter.messagebox.showinfo("Guess the number", "Correct answer")

def button():
    tkinter.messagebox.showinfo("Guess the number", "Hi " + entry1.get()  +  " Can you guess a number between 1-10?")


label1=tkinter.Label(screen,text="Welcome to our game!",fg="black")
label1.place(x=330, y=20)

label2=tkinter.Label(screen,text="What's your name?",fg="black")
label2.place(x=150, y=100)

entry1=tkinter.Entry(screen)
entry1.place(x=150, y=130)

button1=tkinter.Button(screen,text="OK",bg="grey",fg="black", width=4, height=2, command=button )
button1.place(x=480, y=120)

label2=tkinter.Label(screen,text="Take a guess",fg="black")
label2.place(x=150,y=235)

entry2=tkinter.Entry(screen)
entry2.place(x=240, y=235)

Button2=tkinter.Button(screen,text="Guess",fg="black", width=4, height=2,command=guess_the_number )
Button2.place(x=480,y=230)


screen.mainloop()







