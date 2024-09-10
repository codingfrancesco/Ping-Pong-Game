import turtle
from ball import Ball
from rod import Rod

ROD_HEIGHT = 100  # Assuming a fixed height for the rods

rod = Rod(260, 'red')
rod2 = Rod(-260, 'blue')
turtle.listen()

turtle.onkeypress(rod.move_up, "Up")
turtle.onkeypress(rod.move_down, "Down")
turtle.onkeypress(rod2.move_up, "w")
turtle.onkeypress(rod2.move_down, "s")

ball = Ball()

def check_collision(rod, ball):
    rod_top = rod.ycor() + ROD_HEIGHT / 2
    rod_bottom = rod.ycor() - ROD_HEIGHT / 2
    
    if (abs(ball.xcor() - rod.xcor()) < 20 and
        rod_bottom < ball.ycor() < rod_top):
        ball.bounce_x()
        # Adjust ball's y-velocity based on where it hits the rod
        relative_intersect_y = (rod.ycor() - ball.ycor()) / (ROD_HEIGHT / 2)
        normalized_relative_intersect_y = relative_intersect_y / (ROD_HEIGHT / 2)
        new_y_velocity = -normalized_relative_intersect_y * 5
        
        # Update ball's y-velocity if your Ball class supports it
        if hasattr(ball, 'set_y_velocity'):
            ball.set_y_velocity(new_y_velocity)
        else:
            # If set_y_velocity doesn't exist, we'll modify the y-direction directly
            ball.sety(ball.ycor() + new_y_velocity)

while True:
    ball.move()
    
    # Wall collisions
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    # Game over condition
    if ball.xcor() > 290 or ball.xcor() < -290:
        turtle.write("Game Over!", align="center", font=("Arial", 30, "bold"))
        break
    
    # Check collisions with both rods
    check_collision(rod, ball)
    check_collision(rod2, ball)
    
    # Update the screen
    turtle.update()

turtle.mainloop()