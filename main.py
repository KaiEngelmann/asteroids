import pygame 
from constants import *
from player import Player

def main():
    pygame.init()
    


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # creates object for FPS
    fps = pygame.time.Clock()
    dt = 0

    # Creates the game object player

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # creates game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        # dt limits loop to 60 FPS

        dt = fps.tick(60) / 1000

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()