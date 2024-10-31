import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.radius = radius
        self.cooldown = 0
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        if self.cooldown > 0:
            self.cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)
        

        

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if self.cooldown > 0:
            return
        else:
            direction = pygame.Vector2(0, 1) 
            direction = direction.rotate(self.rotation) 
            velocity = direction * PLAYER_SHOOT_SPEED

            shot = Shot(self.position.x, self.position.y)
            shot.velocity = velocity
            self.cooldown = PLAYER_SHOOT_COOLDOWN
            return shot
            
        
