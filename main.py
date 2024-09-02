import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    delta_time = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
            
    Player.containers = (updateable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    Shot.containers = (updateable, drawable, shots)

    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)

    AsteroidField()

    # Game loop
    while True:
        # Exit strategy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update_object in updateable:
            update_object.update(delta_time)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                return

        # Rendering
        screen.fill("black")
        for draw_object in drawable:
            draw_object.draw(screen)
        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()