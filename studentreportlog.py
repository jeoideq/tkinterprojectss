import tkinter
import tkinter.filedialog



screen=tkinter.Tk()
screen.geometry("700x400")
screen.title("Student Report Log")

student_log={}

def edit():
    index=listbox.curselection()
    name=listbox.get(index)
    record=student_log[name]
    entry1.insert(0,name)
    entry2.insert(0,record[0])
    entry3.insert(0,record[1])
    entry4.insert(0,record[2])
    entry5.insert(0,record[3])

def delete():
    index=listbox.curselection()
    name=listbox.get(index)
    del student_log[name]
    update_listbox()



def open():
    global student_log
    file1=tkinter.filedialog.askopenfile()
    if file1!=None:
        student_log=eval(student_log,file=file1)
        update_listbox()



def update_add():
    name=entry1.get()
    rollnumber=entry2.get()
    science_marks=entry3.get()
    math_marks=entry4.get()
    percentage=entry5.get()
    student_log[name]=[rollnumber,science_marks,math_marks,percentage]
    update_listbox()
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)
    entry5.delete(0, tkinter.END)



def save():
    file1=tkinter.filedialog.asksaveasfile()
    if file1!=None:
        print(student_log,file=file1)


def update_listbox():
    listbox.delete(0,tkinter.END)
    keys=student_log.keys()
    for key in keys:
        listbox.insert(tkinter.END, key )



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

button1=tkinter.Button(screen, text="Edit", fg="black", command=edit)
button1.grid(row=8, column=1)

button2=tkinter.Button(screen, text="Delete", fg="black" , command=delete)
button2.grid(row=8, column=2, padx=20)

button3=tkinter.Button(screen, text="Open", fg="black", command=open)
button3.grid(row=8, column=3, padx=20)

button4=tkinter.Button(screen, text="Update/Add", fg="black", command=update_add)
button4.grid(row=8, column=4, padx=20)

button5=tkinter.Button(screen, text="Save", fg="black" , command=save)
button5.grid(row=8, column=5, padx=20, pady=90)

#listbox 

listbox=tkinter.Listbox(screen , width=70 )
listbox.grid(row=5, column=1, padx=10, columnspan=5)


screen.mainloop()



