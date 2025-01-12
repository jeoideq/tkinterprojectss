import tkinter

screen=tkinter.Tk()
screen.geometry("500x400")
screen.title("My Adress Book")

#title

Label1=tkinter.Label(screen, text="My Adress Book", fg="black")
Label1.grid(row=1, column=2, padx=30)

#button

button1=tkinter.Button(screen, text="Open", fg="black")
button1.grid(row=1, column=3)

#listbox

listbox=tkinter.Listbox(screen,width=20, height=10)
listbox.grid(row=2, column=1, columnspan=2, rowspan=5)


#labels

Label1=tkinter.Label(screen, text="Name:", fg="black")
Label1.grid(row=2, column=3)

label2=tkinter.Label(screen, text="Adress:", fg="black")
label2.grid(row=3, column=3)

Label3=tkinter.Label(screen, text="Mobile:", fg="black")
Label3.grid(row=4, column=3)

Label4=tkinter.Label(screen, text="Email:", fg="black")
Label4.grid(row=5, column=3)

Label5=tkinter.Label(screen, text="Birthday:", fg="black")
Label5.grid(row=6, column=3)




entry1=tkinter.Entry(screen, width=10)
entry1.grid(row=2, column=4)

entry2=tkinter.Entry(screen, width=10)
entry2.grid(row=3, column=4)

entry3=tkinter.Entry(screen, width=10)
entry3.grid(row=4, column=4)

entry4=tkinter.Entry(screen, width=10)
entry4.grid(row=5, column=4)

entry5=tkinter.Entry(screen, width=10)
entry5.grid(row=6, column=4)


#buttons 

button1=tkinter.Button(screen, text="Edit", fg="black")
button1.grid(row=7, column=1)

button1=tkinter.Button(screen, text="Delete", fg="black")
button1.grid(row=7, column=2)

button1=tkinter.Button(screen, text="Update/Add", fg="black")
button1.grid(row=7, column=4)

button1=tkinter.Button(screen, text="Save", fg="black", width=15)
button1.grid(row=8, column=2, columnspan=2)





screen.mainloop()