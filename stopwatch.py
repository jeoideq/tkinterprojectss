import tkinter 

screen=tkinter.Tk()
screen.geometry("300x200")
screen.title("Stopwatch")

hour=tkinter.StringVar()

minutes=tkinter.StringVar()

sec=tkinter.StringVar()
hour.set("1")
minutes.set("0")
sec.set("0")

entry1=tkinter.Entry(screen, width=5, textvariable=hour)
entry1.grid(row=1, column=1, padx=20)

entry2=tkinter.Entry(screen, width=5, textvariable=minutes)
entry2.grid(row=1, column=2, padx=20)

entry3=tkinter.Entry(screen, width=5, textvariable=sec)
entry3.grid(row=1, column=3, pady=50, padx=20)

button=tkinter.Button(screen, text="Start")
button.grid(row=2, column=2)

screen.mainloop()