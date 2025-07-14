from circleshape import *
from constants import *
from shot import *
import os
import pygame
from pathlib import Path
import sounds

SPACESHIP_IMAGE = None


class Player(CircleShape):

    SPACESHIP_IMAGE = None
    
    @classmethod
    def load_spaceship(cls):
        base_path = Path(__file__).parent  # Folder where this Python file lives
        image_path = base_path / "assets" / "player.png"        
        original_image = pygame.image.load(str(image_path)).convert_alpha()
        cls.SPACESHIP_IMAGE = pygame.transform.flip(original_image, False, True)
    def __init__(self, x , y, image=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.position = pygame.Vector2(x, y)
        self.original_image = self.SPACESHIP_IMAGE
        self.update_scaled_image()

    def update_scaled_image(self):
        diameter = self.radius * 2
        self.image = pygame.transform.smoothscale(self.original_image, (int(diameter), int(diameter)))
        self.rect = self.image.get_rect(center=self.position)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rotated_rect)
        self.rect = rotated_rect  # update self.rect to match rotated image position

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
            channel = pygame.mixer.find_channel()
            if sounds.LASER_SOUND and channel:
                channel.play(sounds.LASER_SOUND)


