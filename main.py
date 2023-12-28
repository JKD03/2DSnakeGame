import turtle
import time
import random

delay = 0.05
pdelay=delay

score = 0
high_score = 0

# Setting Window
wn = turtle.Screen()
wn.title("SnakeGame")
wn.setup(width=800, height=800)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = 'stop'
head.hideturtle()

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.hideturtle()

# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.shape('square')
pen.color('black')
pen.goto(0, 360)           # Scoreboard location
pen.write("Score: 0 Highscore: 0", align='center', font=('Arial', 24, 'normal'))    # Initial Score Board

# Snake Body
segments = []

# Game State (intro, ingame)
game_state = 'intro'

def start_game():
    global game_state
    game_state = 'ingame'
def pause_game():
    global delay,pdelay
    if delay > 0:
        pdelay=delay
        delay=10000
    else:
        delay=pdelay


# Functions to Change Direction of the Heads
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'


#Move Head of snake
def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    if head.direction == 'down':
        head.sety(head.ycor() - 20)
    if head.direction == 'right':
        head.setx(head.xcor() + 20)
    if head.direction == 'left':
        head.setx(head.xcor() - 20)


# Game Over Function is called when the snake touches the window boundary or collides with itself
def game_over():
    global delay, score, segment
    head.direction = 'stop'
    time.sleep(1)
    for segment in segments:
        segment.goto(2000, 2000)
    segments.clear()
    head.goto(0, 0)
    score = 0
    score_write()
    delay = 0.05

def score_inc():
    global score, high_score
    score += 1
    if score > high_score:
        high_score += 1


# Writes The Score On the Screen
def score_write():
    pen.clear()    #clear score
    pen.write(f'Score: {score} Highscore: {high_score}', align='center', font=('Arial', 24, 'normal'))


# Key Bindings
wn.listen()
wn.onkeypress(pause_game, 'p')
wn.onkeypress(start_game, 'Return')  # 'Return' corresponds to the Enter key
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

# Main Game Loop
while True:
    wn.update()

    if game_state == 'intro':
        wn.bgpic('MainMenu.gif')
        pen.clear()
    elif game_state == 'ingame':
        wn.bgpic('GrassBackground.gif')
        head.showturtle()
        food.showturtle()
        score_write()

    if head.distance(food) < 20:
        score_inc()
        score_write()

        flag = 0
        x = 0
        y = 0
        while flag == 0:
            flag = 1
            x = random.randint(-380, 380)
            y = random.randint(-380, 350)
            for segment in segments:
                if segment.distance(x, y) < 20:
                    flag = 0
                    break
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.003

    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if head.distance(segment) < 20:
            game_over()
            break

    if head.xcor() < -380:
        head.goto(380, head.ycor())
    if head.xcor() > 380:
        head.goto(-380, head.ycor())
    if head.ycor() < -380:
        head.goto(head.xcor(), 380)
    if head.ycor() > 380:
        head.goto(head.xcor(), -380)

    time.sleep(delay)

wn.mainloop()  # Keeps the Game Window Open