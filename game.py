### These imports are specifically suited for a Windows environment.
from pynput.keyboard import Key, Controller
from os import system, name
mykeyboard = Controller()
import keyboard
import sys

from cursesmenu.items import *
from cursesmenu import *
from curses import panel
import curses

from time import sleep

import math
### End of Imports.

# Window Width & Length
w_width  = 40
w_height = 10

i = 0

# Cells responsible for the drawing of the board.
cells = {}

for i in range(w_height):
    cells[i] = [' '] * w_width
    cells[i][1] = '|'
    cells[i][w_width -2] = '|'

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

paddle1_y = 3
paddle2_y = 4

ball_x = 3
ball_y = 3

x_speed = 1
y_speed = 1

def position_paddle1():
    cells[paddle1_y][1] = 'X'

def position_ball():
    if cells[ball_y][ball_x] != '|':
        cells[ball_y][ball_x] = 'O'

def draw_board():
    for row in cells:
        column = cells[row]
        print(''.join([x for x in column]))
    print(ball_x)

def get_input():
    global paddle1_y
    if keyboard.is_pressed('j'):
        cells[str(paddle1_y)][1] = '|'
        paddle1_y += 1
    if keyboard.is_pressed('k'):
        cells[str(paddle1_y)][1] = '|'
        paddle1_y -= 1
    if keyboard.is_pressed('z'):
        sys.exit()


def game():
    global ball_speed
    global randomness
    global paddle1_y
    global paddle2_y
    global ball_x
    global ball_y
    global x_speed
    global y_speed
    clear()
    while True:
        if ball_x > w_width-3:
            x_speed = -1
        if ball_x < 3:
            x_speed = 1
        if ball_y < 1:
            y_speed = 1
        if ball_y > w_height-2:
            y_speed = -1
        ball_x += x_speed
        ball_y += y_speed
        draw_board()
        get_input()
        position_paddle1()
        cells[(ball_y - y_speed)][ball_x - x_speed] = ' '
        position_ball()
        sleep(0.1)
        clear()

menu = CursesMenu("Title", "Subtitle")
function_item = FunctionItem("Play the Game", game)

menu.append_item(function_item)

if __name__ == '__main__':                                                       
    menu.show()
