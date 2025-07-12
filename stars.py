import random
from constants import *

NUM_STARS = 100

# Generate star positions and base brightness
stars = []
for _ in range(NUM_STARS):
    x = random.randint(0, SCREEN_WIDTH - 1)
    y = random.randint(0, SCREEN_HEIGHT - 1)
    base_brightness = random.randint(150, 255)
    stars.append([x, y, base_brightness])
