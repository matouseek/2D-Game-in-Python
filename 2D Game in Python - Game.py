import pygame
# I'll be using os in order to load my images
import os

# Init and Window Creation, Clock init
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

# Draw game
def draw_game():
    clock.tick(60)
    win.fill((0, 0, 0))
    pygame.display.update()

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False