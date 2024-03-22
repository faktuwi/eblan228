import turtle
import time
import random
from tkinter import*
from random import choice
import customtkinter
from tkinter import messagebox

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

def Exit():
    exit()

def snake():
    delay = 0.08

    # Score
    score = 0
    high_score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.title("ИГРЫ")
    wn.bgcolor("white")
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("green")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("circle")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=('Comic Sans MS',14,'bold'))

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")

    # Main game loop
    while True:
        wn.update()

        # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            wn.bgcolor("red")
            time.sleep(1)
            turtle.bye()
            messagebox.showerror("anta baka", "Наматало на столб")

             


        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                wn.bgcolor("red")
                time.sleep(1)
                turtle.bye()
                messagebox.showerror("anta baka", "Ты сам себя схавал(((")
        time.sleep(delay)

    wn.mainloop()
      



root = customtkinter.CTk()
root.title('Игры')
root.geometry('300x300')
root.resizable(width=False, height=False)


btn = customtkinter.CTkButton(root, text='Конченая змея', font=('Comic Sans MS',14,'bold'), command=snake)
btn.place (relx=0.5, y=70, anchor=CENTER)

btn = customtkinter.CTkButton(root, text='Вторая игра', font=('Comic Sans MS',14,'bold'), command=snake)
btn.place (relx=0.5, y=105, anchor=CENTER)



root.mainloop()