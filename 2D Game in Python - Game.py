import pygame
# I'll be using os in order to load my images
import os

# Init and Window Creation, Clock init, Background load
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load(os.path.join("Background.png")), (win_width, win_height)) # I scale my background to win_width, win_height using pygame.transform

# Loading Images
guts_idle = [pygame.image.load(os.path.join("guts idle", "guts idle1.png")),
        pygame.image.load(os.path.join("guts idle", "guts idle2.png")),
        pygame.image.load(os.path.join("guts idle", "guts idle3.png")),
        pygame.image.load(os.path.join("guts idle", "guts idle4.png"))
        ]
guts_left = [pygame.image.load(os.path.join("guts run left", "guts run left1.png")),
        pygame.image.load(os.path.join("guts run left", "guts run left2.png")),
        pygame.image.load(os.path.join("guts run left", "guts run left3.png"))
        ]
guts_right = [pygame.image.load(os.path.join("guts run right", "guts run right1.png")),
         pygame.image.load(os.path.join("guts run right", "guts run right2.png")),
         pygame.image.load(os.path.join("guts run right", "guts run right3.png"))
         ]

class Guts:
    def __init__(self, x, y):
        # Coordinates x, y
        self.x = x
        self.y = y

        # Velocities, both x, y
        self.velx = 10
        self.vely = 10

        # Variables for checking which animation to print
        self.face_right = False
        self.face_left = False
        self.idle = True

        # Variables for checking which frame of animation to print
        self.stepIndex = 0
        self.stepIndex_Idle = 0

    def move_guts(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 64: # 'self.x <= win_width - 64' allows me to check whether the character is out of window
            self.x += self.velx
            self.face_right = True
            self.face_left = False
            self.idle = False
        elif userInput[pygame.K_LEFT] and self.x >= 0: # 'self.x >= 0' same thing as above, just with the left side of the window
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
            self.idle = False
        else: # If I'm not pressing anything, the character is in Idle state
            self.face_right = False
            self.face_left = False
            self.idle = True
            self.stepIndex = 0

    def draw(self, win):
        if self.stepIndex >= 6:
            self.stepIndex = 0
        if self.stepIndex_Idle >= 20:
            self.stepIndex_Idle = 0
        if self.face_right:
            win.blit(guts_right[self.stepIndex//2], (self.x, self.y))
            self.stepIndex += 1
        elif self.face_left:
            win.blit(guts_left[self.stepIndex//2], (self.x, self.y))
            self.stepIndex += 1
        elif self.idle:
            win.blit(guts_idle[self.stepIndex_Idle//5], (self.x, self.y))
            self.stepIndex_Idle += 1
# Draw game
def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0 ,0))
    guts.draw(win)
    pygame.display.update()

guts = Guts(250, 290)

# Game loop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Input
    userInput = pygame.key.get_pressed()

    # Movement Guts
    guts.move_guts(userInput)

    draw_game()