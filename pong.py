from os import system, name
# import keyboard
# from pynput.keyboard import Key, Controller
# mykeyboard = Controller()

import math

from time import sleep

winbreadth = 10
winlength = 40

i = 0

cells = {}

# cells = {
#         '0': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '1': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '2': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '3': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '4': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '5': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '6': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
#         '7': [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ']
#         }

for i in range(winbreadth):
    cells[i] = [' '] * winlength
    cells[i][1] = "|"
    cells[i][winlength -2] = "|"

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

ball_speed = 25
randomness = 3

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

# def get_input():
#     global paddle1_y
#     # if keyboard.is_pressed('j'):
#         cells[paddle1_y][1] = '|'
#         paddle1_y += 1
#     # if keyboard.is_pressed('k'):
#         cells[paddle1_y][1] = '|'
#         paddle1_y -= 1
i = 0
while True :
    if ball_x > winlength - 3:
        x_speed = -1
    if ball_x < 2:
        x_speed = 1
    if ball_y < 1:
        y_speed = 1
    if ball_y > winbreadth - 2:
        y_speed = -1
    ball_x += x_speed
    ball_y += y_speed
    draw_board()
    # get_input()
    position_paddle1()
    if cells[ball_y - y_speed][ball_x - x_speed] == 'O':
        cells[ball_y - y_speed][ball_x - x_speed] = ' '
    position_ball()
    #print((' ' * abs(int(math.sin(i)*ball_speed))) + 'O')
    sleep(0.05)
    i += 1
    #i += 1
    clear()


