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
scoreboard=canvas.create_text(60,580,text="0 vs 0", fill="white",font=["arial",25,"normal"])


class Ball():
    def __init__(self,p1,p2):
        self.player1=p1
        self.player2=p2
        self.ball=canvas.create_oval(400,300,430,330,fill="green")
        self.changex=-4
        self.changey=-8
        self.score1=0
        self.score2=0
    def draw(self):
        canvas.move(self.ball,self.changex,self.changey)
        self.cords=canvas.coords(self.ball) 
        if self.cords[0]<0:
            self.score2+=1
            self.changex=4
        if self.cords[2]>800:
            self.score1+=1
            self.changex=-4
        if self.cords[1]<0:
            self.changey=8
        if self.cords[3]>600:
            self.changey=-8
        canvas.itemconfig(scoreboard,text=str(self.score1) + "  vs  " + str(self.score2))
    def check_colision(self):
        self.cords1=canvas.coords(self.player1.rectangle) #player1
        self.cords2=canvas.coords(self.player2.rectangle)#player2
        if self.cords1[1]<self.cords[3] and self.cords1[3]>self.cords[1]:
            if self.cords[0]<self.cords1[2] and self.cords[0]>self.cords1[0]:
                self.changex=4 

        if self.cords2[1]<self.cords[3] and self.cords2[3]>self.cords[1]:
            if self.cords2[0]<self.cords[2] and self.cords2[2]>self.cords[2]:
                self.changex=-4

        

        
                                  



        

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
        self.changey=0
    def move_up(self,event):
        self.changey=-9
    def move_down(self,event):
        self.changey=9

    



class Player2():
    def __init__(self):
        self.rectangle=canvas.create_rectangle(760,20,780,150, fill="white")
        self.changey=0
        canvas.bind_all("k",self.move_up)
        canvas.bind_all("l",self.move_down)
    def move(self):
        canvas.move(self.rectangle,0,self.changey)
        self.cords=canvas.coords(self.rectangle)
        if self.cords[1]<0:
            self.changey=0
        if self.cords[3]>600:
            self.changey=0
        self.changey=0
    def move_up(self,event):
        self.changey=-9
    def move_down(self,event):
        self.changey=9




opponent1=Player1()
opponent2=Player2()
pingpongball=Ball(opponent1,opponent2)
while True:
    pingpongball.draw()
    opponent1.move()
    opponent2.move()
    pingpongball.check_colision()


    screen.update_idletasks()
    screen.update()



screen.mainloop()

