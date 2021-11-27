# I'll be using os in order to load my images
import os

from menu import *

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
guts_att_right = [pygame.image.load(os.path.join("guts attack right", "guts attack right1.png")),
                  pygame.image.load(os.path.join("guts attack right", "guts attack right2.png")),
                  pygame.image.load(os.path.join("guts attack right", "guts attack right3.png")),
                  pygame.image.load(os.path.join("guts attack right", "guts attack right4.png"))
                  ]
guts_att_left = [pygame.image.load(os.path.join("guts attack left", "guts attack left1.png")),
                  pygame.image.load(os.path.join("guts attack left", "guts attack left2.png")),
                  pygame.image.load(os.path.join("guts attack left", "guts attack left3.png")),
                  pygame.image.load(os.path.join("guts attack left", "guts attack left4.png"))
                  ]
dragonslayer_right = [pygame.image.load(os.path.join("dragonslayer right", "dragonslayer right1.png")),
                      pygame.image.load(os.path.join("dragonslayer right", "dragonslayer right2.png")),
                      pygame.image.load(os.path.join("dragonslayer right", "dragonslayer right3.png")),
                      pygame.image.load(os.path.join("dragonslayer right", "dragonslayer right4.png"))
                      ]
dragonslayer_left =  [pygame.image.load(os.path.join("dragonslayer left", "dragonslayer left1.png")),
                      pygame.image.load(os.path.join("dragonslayer left", "dragonslayer left2.png")),
                      pygame.image.load(os.path.join("dragonslayer left", "dragonslayer left3.png")),
                      pygame.image.load(os.path.join("dragonslayer left", "dragonslayer left4.png"))
                      ]

mrakoplas_idle = [pygame.image.load(os.path.join("mrakoplas idle", "mrakoplas1.png")),
        pygame.image.load(os.path.join("mrakoplas idle", "mrakoplas2.png")),
        pygame.image.load(os.path.join("mrakoplas idle", "mrakoplas3.png")),
        pygame.image.load(os.path.join("mrakoplas idle", "mrakoplas4.png")),
        pygame.image.load(os.path.join("mrakoplas idle", "mrakoplas5.png"))
        ]
mrakoplas_left = [pygame.image.load(os.path.join("mrakoplas run left", "mrakoplas run left1.png")),
        pygame.image.load(os.path.join("mrakoplas run left", "mrakoplas run left2.png")),
        pygame.image.load(os.path.join("mrakoplas run left", "mrakoplas run left3.png")),
        pygame.image.load(os.path.join("mrakoplas run left", "mrakoplas run left4.png"))
        ]
mrakoplas_right =[pygame.image.load(os.path.join("mrakoplas run right", "mrakoplas run right1.png")),
         pygame.image.load(os.path.join("mrakoplas run right", "mrakoplas run right2.png")),
         pygame.image.load(os.path.join("mrakoplas run right", "mrakoplas run right3.png")),
        pygame.image.load(os.path.join("mrakoplas run right", "mrakoplas run right4.png"))
        ]
mrakoplas_att_right = [pygame.image.load(os.path.join("mrakoplas attack right", "mrakoplas attack right1.png")),
                       pygame.image.load(os.path.join("mrakoplas attack right", "mrakoplas attack right2.png")),
                       pygame.image.load(os.path.join("mrakoplas attack right", "mrakoplas attack right3.png")),
                       pygame.image.load(os.path.join("mrakoplas attack right", "mrakoplas attack right4.png"))
                      ]
mrakoplas_att_left =  [pygame.image.load(os.path.join("mrakoplas attack left", "mrakoplas attack left1.png")),
                       pygame.image.load(os.path.join("mrakoplas attack left", "mrakoplas attack left2.png")),
                       pygame.image.load(os.path.join("mrakoplas attack left", "mrakoplas attack left3.png")),
                       pygame.image.load(os.path.join("mrakoplas attack left", "mrakoplas attack left4.png"))
                      ]
fireball_right = [pygame.image.load(os.path.join("fireball right", "fireball right1.png")),
                  pygame.image.load(os.path.join("fireball right", "fireball right2.png")),
                  pygame.image.load(os.path.join("fireball right", "fireball right3.png"))
                 ]
fireball_left = [pygame.image.load(os.path.join("fireball left", "fireball left1.png")),
                 pygame.image.load(os.path.join("fireball left", "fireball left2.png")),
                 pygame.image.load(os.path.join("fireball left", "fireball left3.png"))
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
        self.att_check = False
        self.att_right = True
        self.att_left = False

        # Jump check
        self.jump_check = False

        # Variables for checking which frame of animation to print
        self.stepIndex = 0
        self.stepIndex_Idle = 0
        self.stepIndex_Attack = 0

        # Rects
        self.dragonslayer_rect = None
        self.guts_rect = guts_idle[0].get_rect(topleft=(self.x, self.y))

        # Collides
        self.collide_check = False

        #HP
        self.hp = 8

    def move_guts(self, userInput):
        if self.att_check:
            pass
        else:
            if userInput[pygame.K_RIGHT] and self.x <= 800 - 64: # 'self.x <= 800 - 64' allows me to check whether the character is out of window
                self.x += self.velx
                self.guts_rect = guts_idle[0].get_rect(topleft=(self.x, self.y))
                self.face_right = True
                self.face_left = False
                self.idle = False
                self.att_right = True
                self.att_left = False
            elif userInput[pygame.K_LEFT] and self.x >= 0: # 'self.x >= 0' same thing as above, just with the left side of the window
                self.x -= self.velx
                self.guts_rect = guts_idle[0].get_rect(topleft=(self.x, self.y))
                self.face_right = False
                self.face_left = True
                self.idle = False
                self.att_right = False
                self.att_left = True
            else: # If I'm not pressing anything, the character is in Idle state
                self.face_right = False
                self.face_left = False
                self.idle = True
                self.stepIndex = 0

    def attack(self, userInput):
        if userInput[pygame.K_RCTRL] and self.att_check == False:
            self.att_check = True

    def collision(self, enemy_rect, enemy):
        if self.att_check:
            if self.dragonslayer_rect.colliderect(enemy_rect) and self.collide_check == False:
                self.collide_check = True
                enemy.get_dmg()

    def draw(self, win):
        if self.att_check:
            if self.stepIndex_Attack >= 20:
                self.stepIndex_Attack = 0
                self.att_check = False
                self.dragonslayer_rect = None
                self.collide_check = False
            if self.att_right:
                win.blit(dragonslayer_right[self.stepIndex_Attack // 5], (self.x, self.y - 23))
                win.blit(guts_att_right[self.stepIndex_Attack // 5], (self.x, self.y))
                self.dragonslayer_rect = dragonslayer_right[0].get_rect(topleft=(self.x, self.y - 23))
                self.stepIndex_Attack += 1
            elif self.att_left:
                win.blit(dragonslayer_left[self.stepIndex_Attack // 5], (self.x - 30, self.y - 23))
                win.blit(guts_att_left[self.stepIndex_Attack // 5], (self.x, self.y))
                self.dragonslayer_rect = dragonslayer_left[0].get_rect(topleft=(self.x - 30, self.y - 23))
                self.stepIndex_Attack += 1
        else:
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

    def jump(self, userInput):
        if userInput[pygame.K_UP] and self.jump_check is False:
            self.jump_check = True
        if self.jump_check:
            self.y -= self.vely*2
            self.guts_rect = guts_idle[0].get_rect(topleft=(self.x, self.y))
            self.vely -= 1
        if self.vely < -10:
            self.vely = 10
            self.jump_check = False

    def hp_bar(self, win):
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y - 10, 64, 10))
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(self.x, self.y - 10, self.hp*8, 10))
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x, self.y - 10, 64, 10), 2)

    def get_dmg(self):
        if self.hp > 0:
            self.hp -= 1
        else:
            self.hp = 0

class Mrakoplas:
    def __init__(self, x, y):
        # Coordinates x, y
        self.x = x
        self.y = y
        self.fireball_x = 0
        self.fireball_y = 0

        # Velocities
        self.velx = 10
        self.vely = 10
        self.fireball_velx = 2

        # Variables for checking which animation to print
        self.face_right = False
        self.face_left = False
        self.idle = True
        self.att_check = False
        self.att_right = True
        self.att_left = False

        # Variables for checking when an action ends
        self.jump_check = False
        self.fireball_check = False

        # Variables for checking which frame of animation to print
        self.stepIndex = 0
        self.stepIndex_Idle = 0
        self.stepIndex_Attack = 0
        self.stepIndex_fireball = 0

        # Rects
        self.fireball_rect = None
        self.mrakoplas_rect = mrakoplas_idle[0].get_rect(topleft=(self.x, self.y))

        #HP
        self.hp = 8

    def move_mrakoplas(self, userInput):
        if self.att_check: # Character stays in place while attacking
            pass
        else:
            if userInput[pygame.K_d] and self.x <= 800 - 64: # 'self.x <= 800 - 64' allows me to check whether the character is out of window
                self.x += self.velx
                self.mrakoplas_rect = mrakoplas_idle[0].get_rect(topleft=(self.x, self.y))
                self.face_right = True
                self.face_left = False
                self.idle = False
                if self.fireball_check == False: #Fix pro to, aby se strany nemenily uprostred letu fireballu
                    self.att_right = True
                    self.att_left = False
            elif userInput[pygame.K_a] and self.x >= 0: # 'self.x >= 0' same thing as above, just with the left side of the window
                self.x -= self.velx
                self.mrakoplas_rect = mrakoplas_idle[0].get_rect(topleft=(self.x, self.y))
                self.face_right = False
                self.face_left = True
                self.idle = False
                if self.fireball_check == False: #Fix pro to, aby se strany nemenily uprostred letu fireballu
                    self.att_right = False
                    self.att_left = True
            else: # If I'm not pressing anything, the character is in Idle state
                self.face_right = False
                self.face_left = False
                self.idle = True
                self.stepIndex = 0

    def attack(self, userInput):
        if userInput[pygame.K_SPACE] and self.fireball_check == False:
            self.att_check = True

    def collision(self, enemy_rect, enemy):
        if self.fireball_check:
            if self.fireball_rect.colliderect(enemy_rect):
                enemy.get_dmg()
                self.fireball_check = False

    def fireball(self, win):
        if -20<self.fireball_x<800:
            if self.att_right and self.fireball_check:
                win.blit(fireball_right[self.stepIndex_fireball//5], (self.fireball_x, self.fireball_y))
                self.fireball_x += self.fireball_velx
                self.fireball_rect = fireball_right[0].get_rect(topleft=(self.fireball_x, self.fireball_y))
                self.stepIndex_fireball += 1
                if self.stepIndex_fireball == 15:
                    self.stepIndex_fireball = 0
            elif self.att_left and self.fireball_check:
                win.blit(fireball_left[self.stepIndex_fireball//5], (self.fireball_x, self.fireball_y))
                self.fireball_rect = fireball_left[0].get_rect(topleft=(self.fireball_x, self.fireball_y))
                self.fireball_x -= self.fireball_velx
                self.stepIndex_fireball += 1
                if self.stepIndex_fireball == 15:
                    self.stepIndex_fireball = 0
        else:
            self.fireball_check = False
            self.stepIndex_fireball = 0

    def draw(self, win):
        if self.att_check:
            if self.stepIndex_Attack >= 20:
                self.stepIndex_Attack = 0
                self.att_check = False
                self.fireball_check = True
                if self.att_right:
                    self.fireball_x, self.fireball_y = self.x + 50, self.y + 20
                elif self.att_left:
                    self.fireball_x, self.fireball_y = self.x, self.y + 20
            if self.att_right:
                win.blit(mrakoplas_att_right[self.stepIndex_Attack//5], (self.x, self.y))
                self.stepIndex_Attack += 1
            elif self.att_left:
                win.blit(mrakoplas_att_left[self.stepIndex_Attack//5], (self.x, self.y))
                self.stepIndex_Attack += 1
        else:
            if self.stepIndex >= 16:
                self.stepIndex = 0
            if self.stepIndex_Idle >= 25:
                self.stepIndex_Idle = 0
            if self.face_right:
                win.blit(mrakoplas_right[self.stepIndex // 4], (self.x, self.y))
                self.stepIndex += 1
            elif self.face_left:
                win.blit(mrakoplas_left[self.stepIndex // 4], (self.x, self.y))
                self.stepIndex += 1
            elif self.idle:
                win.blit(mrakoplas_idle[self.stepIndex_Idle // 5], (self.x, self.y))
                self.stepIndex_Idle += 1

    def jump(self, userInput):
        if userInput[pygame.K_w] and self.jump_check is False:
            self.jump_check = True
        if self.jump_check:
            self.y -= self.vely*2
            self.mrakoplas_rect = mrakoplas_idle[0].get_rect(topleft=(self.x, self.y))
            self.vely -= 1
        if self.vely < -10:
            self.vely = 10
            self.jump_check = False

    def hp_bar(self, win):
        pygame.draw.rect(win, (255, 0, 0), pygame.Rect(self.x, self.y - 10, 64, 10))
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(self.x, self.y - 10, self.hp*8, 10))
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x, self.y - 10, 64, 10), 2)

    def get_dmg(self):
        if self.hp > 0:
            self.hp -= 1
        else:
            self.hp = 0

class Game:
    def __init__(self):
        self.main_menu = MainMenu(self)

        self.guts = Guts(250, 290)
        self.mrakoplas = Mrakoplas(400, 290)

        self.clock = pygame.time.Clock()

        # I scale my background to win_width, win_height using pygame.transform
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("Background.png")), (self.main_menu.width, self.main_menu.height))

        self.userInput = None

    def draw_guts(self):
        self.guts.attack(self.userInput)
        self.guts.move_guts(self.userInput)
        self.guts.jump(self.userInput)
        self.guts.draw(self.main_menu.win)
        self.guts.collision(self.mrakoplas.mrakoplas_rect, self.mrakoplas)
        self.guts.hp_bar(self.main_menu.win)

    def draw_mrakoplas(self):
        self.mrakoplas.attack(self.userInput)
        self.mrakoplas.move_mrakoplas(self.userInput)
        self.mrakoplas.jump(self.userInput)
        self.mrakoplas.draw(self.main_menu.win)
        self.mrakoplas.fireball(self.main_menu.win)
        self.mrakoplas.collision(self.guts.guts_rect, self.guts)
        self.mrakoplas.hp_bar(self.main_menu.win)

    def Game_loop(self):
        while self.main_menu.game_running:
            self.clock.tick(60)
            self.check_events()
            self.main_menu.win.fill(self.main_menu.black)
            self.main_menu.win.blit(self.background, (0, 0))
            self.userInput = pygame.key.get_pressed()

            self.draw_guts()
            self.draw_mrakoplas()

            pygame.display.update()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main_menu.game_running = False
                self.main_menu.mm_running = False