import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(2,2)
        self.color("red")
        self.pos_x = 0
        self.pos_y = 100
        self.speed_x = 1
        self.speed_y = 1
        self.goto(self.pos_x,self.pos_y)
    def move(self):
        self.pos_x = self.xcor() + self.speed_x
        self.pos_y = self.ycor() + self.speed_y
        self.goto(self.pos_x, self.pos_y)

    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

if __name__ == "__main__":
    ball    = Ball()

    while(True):
        ball.move()
        if ball.ycor() > 260 or ball.ycor() < -240:
            ball.bounce_y()
        if ball.xcor() > 290 or ball.xcor() < -290:
            ball.bounce_x()

    turtle.mainloop()