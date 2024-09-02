import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    delta_time = 0

    # Game loop
    while True:
        # Exit strategy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Black screen
        screen.fill("black")
        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()