from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, round_number=1):
        super().__init__(x, y, radius)
        self.round_number = round_number
    def draw(self, screen):
        color = (255, 255, 255)
        center = (self.position.x, self.position.y)

        pygame.draw.circle(screen, color, center, self.radius, width=2)

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

