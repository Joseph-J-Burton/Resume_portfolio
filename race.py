from turtle import Turtle, Screen
import random


race_is_on = False
screen = Screen()
message = Turtle()
message.hideturtle()
message.penup()
message.color("black")

screen.title("Turtle Races")
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color: {colors} ")
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_is_on = False
            # add in the game over message
            message.goto(0, 30)
            message.write(arg="GAME OVER", align="center", font=("Arial", 20, "normal"))
            message.goto(0, -100)
            message.write(arg="Click to close", align="center", font=("Arial", 10, "normal"))
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won!")
                message.goto(0, -20)
                message.write(arg=f"You've won! The {winning_color} turtle won!", align="center",
                              font=("Arial", 12, "normal"))
            else:
                print(f"You've lost! The {winning_color} turtle won!")
                message.goto(0, -40)
                message.write(arg=f"You've lost! The {winning_color} turtle won!", align="center",
                              font=("Arial", 12, "normal"))

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
