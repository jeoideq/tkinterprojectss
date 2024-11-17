import tkinter

screen=tkinter.Tk()
screen.geometry("800x400")
screen.title("tkinter")

label1=tkinter.Label(screen,text="Create an account",bg="blue",fg="white",width=20,height=3)
label1.pack()
label2=tkinter.Label(screen,text="it's quick and easy", bg="blue",fg="white")
label2.pack()

entry=tkinter.Entry(screen)
entry.pack()

button=tkinter.Button(screen,text="done")
button.pack()


screen.mainloop()