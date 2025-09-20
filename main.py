import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # initialize the pygame module
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock to restrict game to draw a maximum of 60 times per second
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
         # --- Update all sprites in updatable ---
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        # --- Draw all sprites in drawable individually ---
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) # pause the game loop until 1/60th of a second has passed
        dt = delta_time / 1000 # milliseconds to seconds

if __name__ == "__main__":
    main()
