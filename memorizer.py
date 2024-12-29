import tkinter
import tkinter.filedialog

screen=tkinter.Tk()
screen.geometry("400x300")
screen.title("Memorizer")

def open():
    opened=tkinter.filedialog.askopenfile()
    if opened!=None:
        datas=opened.readlines()
        for data in datas:
            listbox.insert(tkinter.END,data)

def delete():
    selected=listbox.curselection()
    listbox.delete(selected)
def save():
    stored=tkinter.filedialog.asksaveasfile()
    if stored!=None:
        items= listbox.get(0,tkinter.END)
        for item in items:
            print(item,file=stored)

    

def add():
    adding=str(entry.get())
    listbox.insert(tkinter.END,adding)
    entry.delete(0,tkinter.END)





button1=tkinter.Button(screen, text="OPEN", command=open)
button1.grid(row=1, column=1)

button2=tkinter.Button(screen, text="DELETE", command=delete)
button2.grid(row=1, column=2)

button3=tkinter.Button(screen, text="SAVE", command=save)
button3.grid(row=1, column=3)

button4=tkinter.Button(screen, text="ADD", command=add)
button4.grid(row=2, column=3)

entry=tkinter.Entry(screen)
entry.grid(row=2, column=1, columnspan=2)

listbox=tkinter.Listbox(screen,width=25)
listbox.grid(row=3, column=1, columnspan=3)

screen.mainloop()