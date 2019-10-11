import sys
from os import system, name
import keyboard
from pynput.keyboard import Key, Controller
mykeyboard = Controller()

from cursesmenu import *
from cursesmenu.items import *

import math

import curses

from curses import panel

from time import sleep

i = 0

cells = {
        '0': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '1': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '2': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '3': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '4': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '5': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '6': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
        '7': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ']
        }

    


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def position_paddle1():
    cells[str(paddle1_y)][1] = 'X'

def position_ball():
    cells[str(ball_y)][ball_x] = ball_sprite


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

def check_collisions():
    if ball_x < 7:
        ball_sprite = 'L'
    elif ball_x > 7:
        ball_sprite = 'R'

ball_speed = 25
randomness = 3

paddle1_y = 3
paddle2_y = 4

ball_x = 3
ball_y = 3

x_speed = 1
y_speed = 1

ball_sprite = 'O'

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
        if ball_x > 10:
            x_speed = -1
        if ball_x < 3:
            x_speed = 1
        if ball_y < 1:
            y_speed = 1
        if ball_y > 6:
            y_speed = -1
        ball_x += x_speed
        ball_y += y_speed
        check_collisions()
        draw_board()
        get_input()
        position_paddle1()
        cells[str((ball_y - y_speed))][ball_x - x_speed] = ' '
        position_ball()
        sleep(0.1)
        clear()

menu = CursesMenu("Title", "Subtitle")
function_item = FunctionItem("Play the Game", game)

menu.append_item(function_item)

if __name__ == '__main__':                                                       
    menu.show()
