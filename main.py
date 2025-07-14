import pygame 
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import Shot
from buttons import Button
import sys
from stars import *
import sounds

def main():
    pygame.init()
    pygame.mixer.init()
    sounds.load_sounds()
    pygame.mixer.set_num_channels(16)

    music_playing = False
    opening_sound_played = False
    game_over_sound_played = False

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # creates object for FPS
    fps = pygame.time.Clock()
    dt = 0
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)

    Player.load_spaceship()

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

    load_asteroid_images()
    START, PLAYING, GAME_OVER = "start", "playing", "game_over"
    game_state = START
    hud_color = (225, 225, 255)
    score = 0
    lives = 3
    time_since_last_hit = 999
    invincibility_duration = 2
    round_number = 1
    score_for_next_round = 30


    def start_game():
        nonlocal game_state, lives, score, player, asteroid_field, \
        time_since_last_hit, round_number, score_for_next_round, \
        opening_sound_played, game_over_sound_played
        game_state = PLAYING
        lives = 3
        score = 0
        time_since_last_hit = 999
        round_number = 1
        score_for_next_round = 30

        opening_sound_played = False
        game_over_sound_played = False

        # Reset game objects
        for sprite in updatable:
            sprite.kill()

        player = Player(x, y)
        asteroid_field = AsteroidField()

    start_button = Button("Start Game", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 25, 200, 50, font, start_game)
    restart_button = Button("Play Again", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50, font, start_game)
    stars = generate_stars()
    # creates game loop
    while True:
        time_since_last_hit += dt
        player_hit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        draw_stars(stars, screen)

        if game_state == START:
            if not opening_sound_played:
                sounds.OPENING_SOUND.play()
                opening_sound_played = True

            start_button.handle_event(event)
        elif game_state == GAME_OVER:
            if not game_over_sound_played:
                sounds.OPENING_SOUND.play()
                game_over_sound_played = True
            restart_button.handle_event(event)

        if game_state == START:
            title_text = font.render("ASTEROIDS", True, (255, 255, 255))
            screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 100))
            start_button.draw(screen)

        elif game_state == GAME_OVER:
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 100))
            screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 150))
            restart_button.draw(screen)
        elif game_state == PLAYING:
            player_hit = False
            if not music_playing:
                pygame.mixer.stop()
                sounds.play_background_music()
                music_playing = True
        

            updatable.update(dt)
            if time_since_last_hit > invincibility_duration:
                for sprite in asteroid_group:
                    if sprite.collisions(player) == True:
                        player_hit = True
                        break
            if player_hit:
                lives -= 1
                time_since_last_hit = 0
                sounds.EXPLOSION_SOUND.play()
                player.kill()
                player = Player(x, y)
                print(f"{lives} Lives Remaining")

            if lives <= 0:
                print("Game Over!")
                sounds.stop_music()
                music_playing = False
                game_state = GAME_OVER
            for asteroid in asteroid_group:
                for shot in shot_group:
                    if asteroid.collisions(shot) == True:
                        asteroid.split()
                        shot.kill()
                        score += 1
                        sounds.EXPLOSION_SOUND.play()
            if score >= score_for_next_round:
                round_number += 1
                score_for_next_round += 30
                asteroid_field.next_round()
            for sprite in drawable:
                sprite.draw(screen)

            lives_text = font.render(f"Lives: {lives}", True, hud_color)
            score_text = font.render(f"Score: {score}", True, hud_color)
            round_text = font.render(f"Round {round_number}", True, hud_color)
            screen.blit(round_text, (SCREEN_WIDTH // 2 - round_text.get_width() // 2, 10))
            screen.blit(lives_text, (10, 10)) 
            screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() -10, 10))
        pygame.display.flip()
        # dt limits loop to 60 FPSs

        dt = fps.tick(60) / 1000
        
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
