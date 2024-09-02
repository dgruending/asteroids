import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    delta_time = 0
            
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Exit strategy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(delta_time)

        # Rendering
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()