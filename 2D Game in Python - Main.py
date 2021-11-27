from game import *

g = Game()

if __name__ == '__main__':
    while g.main_menu.mm_running:
        g.main_menu.MainMenu_loop()