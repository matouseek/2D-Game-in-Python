import pygame

class MainMenu:
    def __init__(self, game):
        pygame.init()

        self.clock = pygame.time.Clock()

        #Widths and heights
        self.width = 800
        self.height = 400
        self.mid_w = self.width/2
        self.mid_h = self.height/2

        self.win = pygame.display.set_mode((self.width, self.height))

        #Variables for checking loops
        self.mm_running = True
        self.game_running = False
        self.end_running = False

        #Colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        self.game = game

        #Text positions
        self.mmx, self.mmy = self.mid_w, self.mid_h - 70
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.quitx, self.quity = self.mid_w, self.mid_h + 100

        #Text colors
        self.mm_color = self.white
        self.start_color = self.white
        self.quit_color = self.white

        #Rectangles for collision
        self.startText_rect = None
        self.quitText_rect = None
        self.mouse_pos = None

    def draw_text(self, text, size, x, y, text_color):
        self.font = pygame.font.Font('8-BIT WONDER.TTF', size)
        self.text = self.font.render(text, True, text_color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.win.blit(self.text, self.textRect)
        return self.textRect

    def MainMenu_loop(self):
        while self.mm_running:
            self.clock.tick(60)
            self.win.fill(self.black)
            self.draw_text('main menu', 50, self.mmx, self.mmy, self.mm_color)
            self.startText_rect = self.draw_text('start', 50, self.startx, self.starty, self.start_color)
            self.quitText_rect = self.draw_text('quit', 50, self.quitx, self.quity, self.quit_color)
            self.check_events()
            pygame.display.update()

    def end_loop(self):
        while self.end_running:
            self.clock.tick(60)
            self.win.fill(self.black)

            if self.game.mrakoplas.hp <= 0:
                self.draw_text('guts wins', 50, self.mid_w, self.mid_h - 70, self.white)
            elif self.game.guts.hp <= 0:
                self.draw_text('mrakoplas wins', 50, self.mid_w, self.mid_h - 70, self.white)

            self.draw_text('press enter to continue', 20, self.mid_w, self.mid_h + 50, self.white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    self.mm_running = False
                    self.end_running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:

                        self.game.mrakoplas.__init__(400, 290)
                        self.game.guts.__init__(250, 290)

                        self.game.background = self.game.pick_map()

                        self.start_color = self.white

                        self.game_running = False
                        self.end_running = False

    def check_events(self):
        self.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.mm_running = False
                self.game_running = False

            if self.startText_rect.collidepoint(self.mouse_pos):
                self.start_color = self.red
                if event.type == pygame.MOUSEBUTTONUP:
                    self.game_running = True
                    self.game.Game_loop()
            else:
                self.start_color = self.white

            if self.quitText_rect.collidepoint(self.mouse_pos):
                self.quit_color = self.red
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mm_running = False
            else:
                self.quit_color = self.white