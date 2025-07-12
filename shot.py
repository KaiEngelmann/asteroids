from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(velocity)
    def draw(self, screen):
        outer_color = (255, 140, 0)  # orange
        inner_color = (255, 255, 0)  # yellow
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, outer_color, center, self.radius)
        pygame.draw.circle(screen, inner_color, center, self.radius // 2)


    def update(self, dt):
            
        self.position += self.velocity * dt
