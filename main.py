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
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)

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
    hud_color = (225, 225, 255)
    score = 0
    lives = 3
    time_since_last_hit = 999
    invincibility_duration = 2 
    # creates game loop
    while True:
        time_since_last_hit += dt
        player_hit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        if time_since_last_hit > invincibility_duration:
            for sprite in asteroid_group:
                if sprite.collisions(player) == True:
                    player_hit = True
                    break
        if player_hit:
            lives -= 1
            time_since_last_hit = 0
            player.kill()
            player = Player(x, y)
            print(f"{lives} Lives Remaining")

        if lives <= 0:
            print("Game Over!")
            sys.exit()
        for asteroid in asteroid_group:
            for shot in shot_group:
                if asteroid.collisions(shot) == True:
                    asteroid.split()
                    shot.kill()
                    score += 1
        for sprite in drawable:
            sprite.draw(screen)

        lives_text = font.render(f"Lives: {lives}", True, hud_color)
        score_text = font.render(f"Score: {score}", True, hud_color)
        
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() -10, 10))
        pygame.display.flip()
        # dt limits loop to 60 FPS

        dt = fps.tick(60) / 1000

    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()