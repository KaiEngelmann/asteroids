from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        color = (255, 255, 255)
        center = (self.position.x, self.position.y)

        pygame.draw.circle(screen, color, center, self.radius, width=2)

    def update(self, dt):
            
        self.position += self.velocity * dt
