from circleshape import *
from constants import *
import random
import os
import pygame

ASTEROID_IMAGES = []
def load_asteroid_images():
    global ASTEROID_IMAGES
    paths = [f"D:/Python Projects/asteroids/asteroid_{i}.png" for i in range(2, 5)]
    ASTEROID_IMAGES = [pygame.image.load(p).convert_alpha() for p in paths]

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, round_number=1):
        super().__init__(x, y, radius)
        self.round_number = round_number
        self.image = random.choice(ASTEROID_IMAGES)
        self.update_scaled_image()

    def update_scaled_image(self):
        # Scale the image to fit the radius (diameter)
        diameter = self.radius * 2
        self.scaled_image = pygame.transform.smoothscale(self.image, (int(diameter), int(diameter)))

    def draw(self, screen):
        rect = self.scaled_image.get_rect(center=(self.position.x, self.position.y))
        screen.blit(self.scaled_image, rect)

    def update(self, dt):
            
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(rand_angle)
        vector2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.round_number)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, self.round_number)
        speed_multiplier = 1.2
        asteroid1.velocity = vector1 * speed_multiplier
        asteroid2.velocity = vector2 * speed_multiplier
