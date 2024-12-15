import tkinter

screen=tkinter.Tk()
screen.geometry("400x700")
screen.title("Memorizer")

def open():
    pass

def delete():
    pass 
def save():
    pass
def add():
    adding=str(entry.get())
    listbox.insert(tkinter.END,adding)




button1=tkinter.Button(screen, text="OPEN", )
button1.grid(row=1, column=1)

button2=tkinter.Button(screen, text="DELETE")
button2.grid(row=1, column=2)

button3=tkinter.Button(screen, text="SAVE")
button3.grid(row=1, column=3)

button4=tkinter.Button(screen, text="ADD", command=add)
button4.grid(row=2, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=1, columnspan=2)

listbox=tkinter.Listbox(screen,width=25)
listbox.grid(row=3, column=1, columnspan=3)

screen.mainloop()