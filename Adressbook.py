import tkinter
import tkinter.filedialog
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("500x400")
screen.title("My Adress Book")


adress_book={}

def update_add():
    name=entry1.get()
    adress=entry2.get()
    mobile=entry3.get()
    email=entry4.get()
    birthday=entry5.get()
    adress_book[name]=[adress,mobile,email,birthday]
    update_listbox()
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)
    entry5.delete(0, tkinter.END)

def edit():
    index=listbox.curselection()
    name=listbox.get(index)
    record=adress_book[name]
    entry1.insert(0,name)
    entry2.insert(0,record[0])
    entry3.insert(0,record[1])
    entry4.insert(0,record[2])
    entry5.insert(0,record[3])



def delete():
    index=listbox.curselection()
    name=listbox.get(index)
    del adress_book[name]
    update_listbox()


def update_listbox():
    listbox.delete(0,tkinter.END)
    keys=adress_book.keys()
    for key in keys:
        listbox.insert(tkinter.END, key)

def save():
    file1=tkinter.filedialog.asksaveasfile()
    if file1!=None:
        print(adress_book,file=file1)

def open():
    global adress_book
    file1=tkinter.filedialog.askopenfile()
    if file1!=None:
        adress_book=eval(file1.read())
        update_listbox()

def display(event):
    index=listbox.curselection()
    name=listbox.get(index)
    record=adress_book[name]
    tkinter.messagebox.showinfo("display","Name: "+name+ "\n Adress" + record[0] + "\n Mobile:" + record[1]  + "\n Email" + record[2] +  " \n Birthday" + record[3])

    



        




#title

Label1=tkinter.Label(screen, text="My Adress Book", fg="black")
Label1.grid(row=1, column=2, padx=30)



#listbox

listbox=tkinter.Listbox(screen,width=20, height=10)
listbox.grid(row=2, column=1, columnspan=2, rowspan=5)
listbox.bind("<<ListboxSelect>>", display)


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

button1=tkinter.Button(screen, text="Open", fg="black", command=open)
button1.grid(row=1, column=3)

button2=tkinter.Button(screen, text="Edit", fg="black", command=edit)
button2.grid(row=7, column=1)

button3=tkinter.Button(screen, text="Delete", fg="black", command=delete)
button3.grid(row=7, column=2)

button4=tkinter.Button(screen, text="Update/Add", fg="black", command=update_add)
button4.grid(row=7, column=4)

button5=tkinter.Button(screen, text="Save", fg="black", width=15, command=save)
button5.grid(row=8, column=2, columnspan=2)







screen.mainloop()