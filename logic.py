lastcol = (0,0)
screenwidth = 7
screenlength = 25 
direction = 0
speed = 1
rev = 0
def collision(paddle1,paddle2,ball,direction,rev):
    if ball == paddle1 or ball == paddle2:
        direction = flip_axis(direction)
        rev = 1 if rev == 0 else 0
    elif ball[0] <= 0 or ball[1] >= screenwidth -1: # top and bottom collisions
        direction = flip_axis(direction)
    elif ball[0] <= 1 or ball[0] >= screenlength -1: # left and right collisions
        endgame()

def flip_axis(slopeval):
    return slopeval * -1

def move(ball,direction,rev):
    return ball[0] + speed, ball[0] + speed
    
    


    
