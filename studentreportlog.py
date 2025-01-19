import tkinter

screen=tkinter.Tk()
screen.geometry("700x400")
screen.title("Student Report Log")

student_log={}

#title

Label1=tkinter.Label(screen, text="STUDENT REPORT LOG", fg="black")
Label1.grid(row=1, column=1)

#label

Label2=tkinter.Label(screen, text="Name:", fg="black")
Label2.grid(row=2, column=1)

Label3=tkinter.Label(screen, text="Roll Number:", fg="black")
Label3.grid(row=3, column=1)

Label4=tkinter.Label(screen, text="Science Mark:", fg="black")
Label4.grid(row=2, column=4)

Label5=tkinter.Label(screen, text="Maths Mark:", fg="black")
Label5.grid(row=3, column=4)

Label6=tkinter.Label(screen, text="Percentage:", fg="black")
Label6.grid(row=4, column=4)


#entry

entry1=tkinter.Entry(screen, width=10)
entry1.grid(row=2, column=2)

entry2=tkinter.Entry(screen, width=10)
entry2.grid(row=3, column=2)

entry3=tkinter.Entry(screen, width=10)
entry3.grid(row=2, column=5)

entry4=tkinter.Entry(screen, width=10)
entry4.grid(row=3, column=5)

entry5=tkinter.Entry(screen, width=10)
entry5.grid(row=4, column=5)


#button

button1=tkinter.Button(screen, text="Edit", fg="black")
button1.grid(row=8, column=1)

button2=tkinter.Button(screen, text="Delete", fg="black")
button2.grid(row=8, column=2, padx=20)

button3=tkinter.Button(screen, text="Open", fg="black")
button3.grid(row=8, column=3, padx=20)

button4=tkinter.Button(screen, text="Update/Add", fg="black")
button4.grid(row=8, column=4, padx=20)

button5=tkinter.Button(screen, text="Save", fg="black")
button5.grid(row=8, column=5, padx=20, pady=90)

#listbox 

listbox=tkinter.Listbox(screen , width=70 )
listbox.grid(row=5, column=1, padx=10, columnspan=5)


screen.mainloop()



