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
    def draw(self):
        canvas.move(self.ball,self.changex,self.changey)
        self.cords=canvas.coords(self.ball)
        if self.cords[0]<0:
            self.changex=4
        if self.cords[2]>800:
            self.changex=-4
        if self.cords[1]<0:
            self.changey=8
        if self.cords[3]>600:
            self.changey=-8
        

class Player1():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(10,20,30,150, fill="white")
        self.changey=0
        canvas.bind_all("a",self.move_up)
        canvas.bind_all("s",self.move_down)
    def move(self):
        canvas.move(self.rectangle,0,self.changey)
        self.cords=canvas.coords(self.rectangle)
        if self.cords[1]<0:
            self.changey=0
        if self.cords[3]>600:
            self.changey=0
    def move_up(self,event):
        self.changey=-4
    def move_down(self,event):
        self.changey=4



class Player2():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(760,20,780,150, fill="white")
        self.player2y=0




pingpongball=Ball()
opponent1=Player1()
opponent2=Player2()
while True:
    pingpongball.draw()
    opponent1.move()
    screen.update_idletasks()
    screen.update()




    









screen.mainloop()

