import tkinter



screen=tkinter.Tk()
screen.geometry("800x400")
screen.title("Celsius to Fahrenheit Converter")

def celsius_to_fahrenheit():
    celsius=int(entry.get())
    fahrenheit=celsius*1.8+32
    label2.config(text="temperature in fahrenheit"+str(fahrenheit))
    



label1=tkinter.Label(screen,text="Celsius -> Fahrenheit",fg="grey", width=30, height=10)
label1.place(x=400, y=50)


entry=tkinter.Entry(screen,text="Enter Temperature in Celsius",fg="grey", width=30)
entry.place(x=200, y=100)


label2=tkinter.Label(screen,text="Temperature in Fahrenheit:",fg="grey", width=50, height=5)
label2.place(x=150, y=150)


button=tkinter.Button(screen,text="Converter",bg="green",fg="grey", width= 30, height="5", command=celsius_to_fahrenheit)
button.place(x=300, y=250)

screen.mainloop()

