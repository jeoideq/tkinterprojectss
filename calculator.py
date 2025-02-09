import tkinter 
import tkinter.ttk

screen=tkinter.Tk()
screen.geometry("400x400")
screen.title("Calculator")

def calculate():
    number1=int(entry1.get())
    number2=int(entry2.get())
    operation=cb.get() 
    result=0

    if operation == "Addition":
        result = number1 + number2
    elif operation == "Subtraction":
        result = number1 - number2
    elif operation == "Multiplication":
        result = number1 * number2
    elif operation == "Division":
        result = number1 / number2
 

    label2.config(text="Your result  " + str(result))

label1=tkinter.Label(screen, text="Calculator", width=10, height=2, fg="black" )
label1.grid(row=1, column=2)

label2=tkinter.Label(screen, width=20, height=2, fg="black" )
label2.grid(row=4, column=2)

entry1=tkinter.Entry(screen)
entry1.grid(row=2, column=2)

entry2=tkinter.Entry(screen)
entry2.grid(row=2, column=3)

button=tkinter.Button(screen,text="Calculate",command=calculate)
button.grid(row=5, column=2)

cb=tkinter.ttk.Combobox(screen, width=10)
cb["values"] = ["Addition", "Subtraction", "Multiplication", "Division"]
cb.grid(row=3, column=2)


screen.mainloop()