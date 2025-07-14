import pygame
from pathlib import Path

base_path = Path(__file__).parent / "assets" / "sounds"

# Sound effect objects
LASER_SOUND = None
EXPLOSION_SOUND = None
OPENING_SOUND = None

# Music file path
BACKGROUND_MUSIC = str(base_path / "background.wav")

def load_sounds():
    global LASER_SOUND, EXPLOSION_SOUND, OPENING_SOUND
    LASER_SOUND = pygame.mixer.Sound(str(base_path / "laser.wav"))
    EXPLOSION_SOUND = pygame.mixer.Sound(str(base_path / "explosion.wav"))
    EXPLOSION_SOUND.set_volume(0.4)
    OPENING_SOUND = pygame.mixer.Sound(str(base_path / "opening.wav"))

def play_background_music(loop=True):
    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.play(-1 if loop else 0)

def stop_music():
    pygame.mixer.music.stop()