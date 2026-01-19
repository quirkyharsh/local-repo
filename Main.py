
from turtle import Turtle,Screen  
import random  
is_race_on=False  
screen=Screen()  
  
screen.setup(width=500,height=400)  
user_guess=screen.textinput(title="make your bet",prompt="which colour turtle will win the race? enter the color:")  
print(user_guess)  
  
colour=["red","green","blue","yellow","black"]  
y_position=[-70,-40,-10,20,50,80]  
turtle_list=[]  
for turtle_index in range(0,5):  
    new_turtle = Turtle("turtle")  
    new_turtle.color(colour[turtle_index])  
    new_turtle.penup()  
    new_turtle.goto(x=-230,y=y_position[turtle_index])  
    turtle_list.append(new_turtle)  
if user_guess:  
    is_race_on=True  
while is_race_on:  
    for turtle in turtle_list:  
        if turtle.xcor()>230:  
            is_race_on=False  
            if turtle.pencolor==user_guess:  
                print("you won")  
            else:  
                print("you lose")  
        random_distance=random.randint(0,10)  
        turtle.forward(random_distance)  
  
  
  
  
screen.exitonclick()
