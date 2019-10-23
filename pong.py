from os import system, name
import sys
from getch import getch
# import keyboard
# from pynput.keyboard import Key, Controller
# mykeyboard = Controller()
import signal
import threading
import time
from time import sleep

winbreadth = 15
winlength = 50

# def boardsize():
#     print("Enter length")
#     winlength = int(input())
#     print("Enter Breadth")
#     winbreadth = int(input())


cells = {}
shameflag = ""
inp = ""
def thread_stdin_read():
    global inp,shameflag
    r = ""
    i = 0
    while shameflag != "}{":
        try:
            # signal.signal(signal.SIGALRM, signal_handler)
            # signal.alarm(1)
            r = getch()
            i += 1
        except Exception:
            pass
        if r != "":
            inp = r
    print("\n")
    exit()


# def signal_handler(signum, frame):
#     raise Exception("Timed out!")

   # Ten seconds

def initial():
    # Intial method to set board size
    e = 0
    # cells[0] = "d|                                              "
    for e in range(winbreadth):
            cells[e] = [' '] * winlength
            cells[e][1] = "|"
            cells[e][winlength -2] = "|"
            cells[e][winlength -1] = "\r"

def clear():
    # Method to clear screen
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# ball_speed = 25
# randomness = 3

# paddle1_y = 3
# paddle2_y = 4

ball_x = 3
ball_y = 3

x_speed = 1
y_speed = 1

player1 = winbreadth//2
player2 = winbreadth//2

# def position_paddle1():
#     cells[paddle1_y][1] = 'X'

def position_player():
    global player1,player2,inp
    inpi = inp
    inp = ""
    if inpi in "wsAB":
        cells[player1][1]="|"
        cells[player1-1][1]="|"
        cells[player1+1][1]="|"
        cells[player2-1][winlength-2]="|"
        cells[player2][winlength-2]="|"
        cells[player2+1][winlength-2]="|"
    if inpi == "w" and player1 > 1:
        player1 -= 1
    elif inpi == "s" and player1 < winbreadth-2:
        player1 += 1
    elif inpi == "A" and player2 > 1:
        player2 -= 1
    elif inpi == "B" and player2 < winbreadth-2:
        player2 += 1
    else:
        pass
    cells[player1][1]="X"
    cells[player1-1][1]="X"
    cells[player1+1][1]="X"
    cells[player2-1][winlength-2]="X"
    cells[player2][winlength-2]="X"
    cells[player2+1][winlength-2]="X"

def position_ball():
    if cells[ball_y][ball_x] != '|' and cells[ball_y][ball_x] != 'X':
        cells[ball_y][ball_x] = "O"


def draw_board():
    print("\r")
    for row in cells:
        column = cells[row]
        print(''.join([x for x in column]))

# def get_input():
#     global paddle1_y
#     # if keyboard.is_pressed('j'):
#         cells[paddle1_y][1] = '|'
#         paddle1_y += 1
#     # if keyboard.is_pressed('k'):
#         cells[paddle1_y][1] = '|'
#         paddle1_y -= 1

def end(loser):
    global shameflag
    shameflag = "}{"
    if loser ==0:
        print("Player 2 Won\r\t")
    else:
        print("Player 1 Won\r\t")
    print("Press Enter to exit")
    exit()
print("Enter any key to start")
m = input()
initial()
x = threading.Thread(target=thread_stdin_read)
x.start()
m = 0
while True :
    m += 1
    position_player()
    if m % 5 == 0:
        if ball_x > winlength - 4:
            x_speed = -1
            if cells[ball_y][winlength-2] != "X":
                # print("N",cells[ball_y][winlength-2],"N")
                end(1)
        if ball_x < 3:
            x_speed = 1
            if cells[ball_y][1] != "X":
                end(0)
                # print("N",cells[ball_y][1],"N")
        if ball_y < 1:
            y_speed = 1
        if ball_y > winbreadth - 2:
            y_speed = -1
        # check
        ball_x += x_speed
        ball_y += y_speed
    if m==0:
        draw_board()
        m += 1
    if cells[ball_y - y_speed][ball_x - x_speed] in ("O"):
        cells[ball_y - y_speed][ball_x - x_speed] = ' '
    position_ball()
    draw_board()
    # r = sys.stdin.read(1)

    # --------- slow code -------------
    # print((' ' * abs(int(math.sin(i)*ball_speed))) + 'O')
    # try:
    #     signal.signal(signal.SIGALRM, signal_handler)
    #     signal.alarm(1)
    #     r = sys.stdin.read(1)
    # except Exception:
    #     pass
    # if type(r) == type("a"):
    #     puck = r
    # else:
    #     puck="0"
        
    


    sleep(0.02)
    clear()


