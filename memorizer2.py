import tkinter
import tkinter.filedialog 

screen=tkinter.Tk()
screen.geometry("400x400")
screen.title("Memorizer")

colors=["red","blue","green","purple","orange","brown","pink","yellow"]


def delete():
    selected=listbox.curselection()
    listbox.delete(selected)

def add():
    added=str(entry.get())
    listbox.insert(tkinter.END, added)
    entry.delete(0, tkinter.END)


def change_bg(event):
    selected_color=listbox.get(tkinter.ACTIVE)
    screen.config(bg=selected_color)
    print("hi")







listbox=tkinter.Listbox(screen, width=35, height=10)
listbox.grid(row=3, column=1, columnspan=6)
listbox.bind("<<ListboxSelect>>", change_bg)
for color in colors:
    listbox.insert(tkinter.END,color)


button2=tkinter.Button(screen,text="Delete", fg="black", width=5, command=delete)
button2.grid(row=1, column=4)

button4=tkinter.Button(screen,text="Add", fg="black", width=5, command=add )
button4.grid(row=2, column=5)

entry=tkinter.Entry(screen, width=20)
entry.grid(row=2, column=2, columnspan=3)

screen.mainloop()