import pygame
from game import Game
from config import *


def main():
    prob = 'astar-2'
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("IUST-PACMAN")
    done = False
    clock = pygame.time.Clock()
    game = Game()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()
