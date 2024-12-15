import tkinter 
import tkinter.ttk

screen=tkinter.Tk()
screen.geometry("700x300")
screen.title("Sushi App")

def order():
    quantity=str(cb2.get())
    select=str(cb1.get())
    size=str(rows.get())
    print(quantity)
    print(select) 
    print(size)
    label4.config(text="You ordered  " + quantity + "  " + select + "  "+ size + "  size")


label1=tkinter.Label(screen, text="Welcome to Sushi Hut", fg="black")
label1.grid(row=1, column=2)

label2=tkinter.Label(screen, text="Select your Fav Sushi:", fg="black")
label2.grid(row=2, column=1)

label3=tkinter.Label(screen, text="Enter Quantity:", fg="black")
label3.grid(row=3, column=1)

label4=tkinter.Label(screen)
label4.grid(row=6, column=2)


rows=tkinter.StringVar()


cb1=tkinter.ttk.Combobox(screen, width=10)
cb1.grid(row=2, column=2)

comboboxvariable1=["Tuna Kimchi Mayo","Tofu Nigiri","California roll", "Prawn nigiris", "Tempura roll" ,"Salmon nigiri", "Avocado Nigiri"]
cb1["values"]=comboboxvariable1

cb2=tkinter.ttk.Combobox(screen, width=10)
cb2.grid(row=3, column=2)

comboboxvariable2=[1,2,3,4,5,6,7,8,9,10]
cb2["values"]=comboboxvariable2


rb1=tkinter.Radiobutton(screen, text="S", variable=rows, value="Small")
rb1.grid(row=2, column=4)

rb2=tkinter.Radiobutton(screen, text="M", variable=rows, value="Medium")
rb2.grid(row=3, column=4)

rb3=tkinter.Radiobutton(screen, text="L", variable=rows, value="Large")
rb3.grid(row=4, column=4)


button=tkinter.Button(screen, text="Order", fg="black", command=order, width=5)
button.grid(row=5, column=2)



screen.mainloop()


            

