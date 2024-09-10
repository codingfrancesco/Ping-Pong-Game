import turtle

class Rod (turtle.Turtle):
    def __init__(self,x,color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.goto(x,0)
        self.color(color)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+10)
        if self.ycor() > 300:
            self.goto(self.xcor(),300)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-10)
        if self.ycor() < -300:
            self.goto(self.xcor(),-300)








if __name__ == "__main__":
    rod = Rod(300,'red')
    rod2 = Rod(-300, 'blue')
    turtle.listen() 

    turtle.onkeypress(rod.move_up,"Up")
    turtle.onkeypress(rod.move_down,"Down")
    turtle.onkeypress(rod2.move_up,"w")
    turtle.onkeypress(rod2.move_down,"s")

    turtle.mainloop()