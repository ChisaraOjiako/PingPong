import turtle 
import random
window = turtle.Screen() 
window.title("Chi's Electric Ping Pong") 
window.bgcolor('black') 
window.setup(width= 800, height = 600) 
window.tracer(0) 
    

# Paddle A
paddle_a = turtle.Turtle() 
paddle_a.speed(0) 
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.color('white') 
paddle_a.penup() 
paddle_a.goto(-350, 0) 


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
starting_velocity = [-.1,.1]
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup() 
ball.goto(0, 0)
ball.dx = random.choice(starting_velocity) 
ball.dy = random.choice(starting_velocity)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle() 
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Times New Roman", 24, "normal")) 

# Score
score_a = 0 
score_b = 0
 

# Functions
def paddle_a_up():
    y = paddle_a.ycor() 
    y += 50 
    paddle_a.sety(y) 
def paddle_a_down(): 
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)

#Ball speed before pause
old_dx = ball.dx
old_dy = ball.dy

# Options Screen
def get_options():
    options_text = turtle.Turtle()
    options_text.goto(0,120)
    options_text.color('red')
    options_text.write('OPTIONS', align="center", font = ('Times New Roman', 18, "normal"))
    options_text.hideturtle()
    play_option =turtle.Turtle()
    play_option.hideturtle()
    play_option.goto(0,100)
    play_option.color('red')
    play_option.write('PLAY(p)', align="center")
    reset_option =turtle.Turtle()
    reset_option.hideturtle()
    reset_option.goto(0,80)
    reset_option.color('red')
    reset_option.write('RESET(r)', align="center")
    clear_screen =turtle.Turtle()
    clear_screen.hideturtle()
    clear_screen.goto(0,60)
    clear_screen.color('red')
    clear_screen.write('Clear Screen(c)', align="center")

    def clear_options():
        options_text.clear()
        play_option.clear()
        reset_option.clear()
        clear_screen.clear()

    def play():
        ball.dx = old_dx
        ball.dy = old_dy
        clear_options()
    
    def reset():
        ball.goto(0,0)
        ball.dx = random.choice(starting_velocity)
        ball.dy = random.choice(starting_velocity)
        clear_options()
    
    window.listen()
    window.onkeypress(clear_options, "c")
    window.onkeypress(play, "p")
    window.onkeypress(reset, 'r')

# Pause button
def pause():
    ball.dx = 0
    ball.dy = 0
    get_options()

window.listen()
window.onkeypress(pause, "space")




#Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w") 
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")



#Main game loop
while True:
    #winsound.PlaySound("pongmusic.mp3", winsound.SND_ASYNC) 
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy) 

    # Border response
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 
        old_dy = ball.dy

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        old_dy = ball.dy

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = random.choice(starting_velocity)
        ball.dy = random.choice(starting_velocity)
        old_dx = ball.dx
        old_dy = ball.dy
        score_a +=1
        pen.clear() 
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("Times New Roman", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = random.choice(starting_velocity)
        ball.dy = random.choice(starting_velocity)
        old_dx = ball.dx
        old_dy = ball.dy
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("Times New Roman", 24, "normal"))

    # Collision
    if ball.xcor() > 340 and ball.xcor() < 360 and ball.ycor() < (paddle_b.ycor() + 50) and ball.ycor() > (paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        if ball.dx > 0:
            ball.dx += .01 
        if ball.dx < 0:
            ball.dx -= .01
        if ball.dy > 0:
            ball.dy += .01 
        if ball.dy < 0:
            ball.dy -= .01  
    
    if ball.xcor() < -340 and ball.xcor() > -360 and ball.ycor() < (paddle_a.ycor() + 50) and ball.ycor() > (paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        if ball.dx > 0:
            ball.dx += .01 
        if ball.dx < 0:
            ball.dx -= .01
        if ball.dy > 0:
            ball.dy += .01 
        if ball.dy < 0:
            ball.dy -= .01  


    
    
            
    
     