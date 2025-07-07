import pygame 
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # creates object for FPS
    fps = pygame.time.Clock()
    dt = 0

    # create groups for game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable, drawable)

    shot_group = pygame.sprite.Group()
    Shot.containers = (shot_group, updatable, drawable)

    AsteroidField.containers = (updatable)
    # creates game object player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)


    asteroid_field = AsteroidField()

    # creates game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for sprite in asteroid_group:
            if sprite.collisions(player) == True:
                print("Game Over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        # dt limits loop to 60 FPS

        dt = fps.tick(60) / 1000

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()