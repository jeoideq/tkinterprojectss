import tkinter
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("800x600")
screen.title("Ping Pong")

screen.config(background="black")
canvas=tkinter.Canvas(screen,background="black",width=800, height=600)
canvas.place(x=0,y=0)
canvas.create_line(400,0,400,600,fill="white",width=4)
canvas.create_oval(350,250,450,350,outline="white", width=4)


class Ball():
    def __init__(self):
        self.ball=canvas.create_oval(400,300,430,330,fill="green")
        self.changex=-4
        self.changey=-8
        self.score1=0
        self.score2=0

class Player1():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(10,20,30,150, fill="white")
        self.player1y=0

class Player2():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(760,20,780,150, fill="white")
        self.player2y=0




pingpongball=Ball()
opponent1=Player1()
opponent2=Player2()









screen.mainloop()

