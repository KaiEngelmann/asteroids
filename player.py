from circleshape import *
from constants import *
from shot import *
import os
import pygame

SPACESHIP_IMAGE = None


class Player(CircleShape):

    SPACESHIP_IMAGE = None
    
    @classmethod
    def load_spaceship(cls):
        original_image = pygame.image.load(r"D:\Python Projects\asteroids\player.png").convert_alpha()
        cls.SPACESHIP_IMAGE = pygame.transform.flip(original_image, False, True)
    def __init__(self, x , y, image=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.original_image = self.SPACESHIP_IMAGE
        self.update_scaled_image()

    def update_scaled_image(self):
        diameter = self.radius * 2
        self.image = pygame.transform.smoothscale(self.original_image, (int(diameter), int(diameter)))

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)

    # rotates the player
    def rotate(self, dt):
        return self.rotation + (PLAYER_TURN_SPEED * dt)
    
    # moves the player
    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * PLAYER_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.shot_timer > 0:
            self.shot_timer -= dt
        if keys[pygame.K_a]:
            self.rotation = self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotation = self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shot_timer <= 0:
            direction = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = direction * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, velocity)
            self.shot_timer = SHOT_CLOCK


