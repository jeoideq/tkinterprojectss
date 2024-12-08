import tkinter 
import tkinter.ttk

screen=tkinter.Tk()
screen.geometry("400x400")
screen.title("Mathematical table")


def box():
    number=int(combobox.get())
    multiples=int(rows.get())
    print(number)
    print(multiples)



label=tkinter.Label(screen, text="Mathematical table")
label.grid(column=2,row=1)

label1=tkinter.Label(screen, text="Number and Range",fg="black", width=20)
label1.grid(column=1, row=2)

combobox=tkinter.ttk.Combobox(screen, width=5)
combobox.grid(column=2,row=2)

rows=tkinter.StringVar()

rb1=tkinter.Radiobutton(screen, text="10", variable=rows,value="10")
rb1.grid(row=2, column=3)

rb2=tkinter.Radiobutton(screen, text="20", variable=rows, value="20" )
rb2.grid(row=3, column=3)

rb3=tkinter.Radiobutton(screen,text="30", variable=rows, value="30")
rb3.grid(row=4, column=3)

button=tkinter.Button(screen, text="Generate", command=box)
button.grid(row=4, column=2)

label2=tkinter.Label(screen)
label2.grid(row=5, column=2)

comboboxvariable=[1,2,3,4,5,6,7,8,9,10]
combobox["values"]=comboboxvariable





screen.mainloop()

