import pygame

from constants import *
from player import Player

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

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
         # --- Update all sprites in updatable ---
        updatable.update(dt)

        # --- Draw all sprites in drawable individually ---
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        delta_time = clock.tick(60) # pause the game loop until 1/60th of a second has passed
        dt = delta_time / 1000 # milliseconds to seconds

if __name__ == "__main__":
    main()
