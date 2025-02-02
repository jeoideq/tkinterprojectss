import tkinter 

class Paint():
    def __init__(self):
        
        self.screen=tkinter.Tk()
        self.screen.geometry("700x700")
        self.screen.title("Paint Appliction")

        self.penbutton=tkinter.Button(self.screen,text="pen")
        self.penbutton.grid(row=1,column=1)

        self.brushbutton=tkinter.Button(self.screen,text="brush")
        self.brushbutton.grid(row=1,column=2)

        self.eraserbutton=tkinter.Button(self.screen,text="eraser")
        self.eraserbutton.grid(row=1,column=3)

        self.colorbutton=tkinter.Button(self.screen,text="color")
        self.colorbutton.grid(row=1,column=4)
        
        self.scale=tkinter.Scale(self.screen, from_=1, to=5, orient="horizontal")
        self.scale.grid(row=1,column=5)

        self.canvas=tkinter.Canvas(self.screen, width=700, height=650, background="white")
        self.canvas.grid(row=2,columnspan=5, column=1)


        self.screen.mainloop()

painting=Paint()











