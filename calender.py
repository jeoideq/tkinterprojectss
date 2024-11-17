import tkinter 

import calendar

screen=tkinter.Tk()
screen.geometry("800x400")  
screen.title("Calender")

def show():
    screen2=tkinter.Tk()
    screen2.geometry("800x400")  
    screen2.title("Calender")

    text=tkinter.Text(screen2,width=90,height=100)
    text.pack()
    
    year=int(entry.get())
    text1=calendar.calendar(year)
    text.insert(tkinter.END,text1)



    screen2.mainloop()



label1=tkinter.Label(screen,text="CALENDER",bg="grey",fg="black", width=25,height=5)
label1.pack()

label2=tkinter.Label(screen,text="Enter year",bg="green",fg="black")
label2.pack()

entry=tkinter.Entry(screen)
entry.pack()

button1 = tkinter.Button(screen, text="Show Calendar", bg="red", fg="black",command=show)  
button1.pack()


button2=tkinter.Button(screen,text="Exit", bg="red", fg="black")
button2.pack()



screen.mainloop()