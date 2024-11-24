import tkinter


screen=tkinter.Tk()
screen.geometry("800x400")
screen.title("weight converter")

def gram_pound_ounce():
    kg=int(entry1.get())
    gram=kg * 1000
    pound=kg * 2.2046 
    ounce=kg * 35.27 
    label5.config(text=gram)
    label6.config(text=pound)
    label7.config(text=ounce)
    button.config(background="orange")

label1=tkinter.Label(screen,text="Enter the weight in Kg",fg="black")
label1.grid(row=1,column=1)

entry1=tkinter.Entry(screen)
entry1.grid(row=1, column=2)

button=tkinter.Button(screen,text="Convert",fg="black", command=gram_pound_ounce)
button.grid(row=1,column=3)

label2=tkinter.Label(screen,text="Gram",fg="black")
label2.grid(row=2,column=1)

label3=tkinter.Label(screen,text="Pounds",fg="black")
label3.grid(row=2,column=2)

label4=tkinter.Label(screen,text="Ounce",fg="black")
label4.grid(row=2,column=3)

label5 = tkinter.Label(screen)
label5.grid(row=3, column=1)

label6 = tkinter.Label(screen)
label6.grid(row=3, column=2)

label7 = tkinter.Label(screen)
label7.grid(row=3, column=3)





screen.mainloop()