from GameUi import GameUi
import pygame

if __name__ == '__main__':
    pygame.init()
    gui = GameUi(True)

    gui.gameloop()
    pygame.quit()
