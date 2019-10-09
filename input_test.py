import pygame

while True:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("w is pressed.")
