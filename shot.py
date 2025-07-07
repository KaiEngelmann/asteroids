from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(velocity)
    def draw(self, screen):
        color = (255, 255, 255)
        center = (self.position.x, self.position.y)

        pygame.draw.circle(screen, color, center, self.radius, width=1)

    def update(self, dt):
            
        self.position += self.velocity * dt
