import random
from constants import *

NUM_STARS = 100

# Generate star positions and base brightness
def generate_stars():    
    stars = []
    for _ in range(NUM_STARS):
        x = random.randint(0, SCREEN_WIDTH - 1)
        y = random.randint(0, SCREEN_HEIGHT - 1)
        base_brightness = random.randint(150, 255)
        stars.append([x, y, base_brightness])
    return stars

def draw_stars(stars, screen):
    for star in stars:
        x, y, base_brightness = star
        flicker = random.randint(-30, 30)
        brightness = max(150, min(255, base_brightness + flicker))
        color = (brightness, brightness, brightness)
        screen.set_at((x, y), color)
