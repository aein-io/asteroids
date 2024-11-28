import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        split_a = self.velocity.rotate(random_angle)
        split_b = self.velocity.rotate(-random_angle)

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_a = Asteroid(
            self.position.x, self.position.y, split_radius)
        asteroid_a.velocity = split_a * 1.2

        asteroid_b = Asteroid(
            self.position.x, self.position.y, split_radius)
        asteroid_b.velocity = split_b * 1.2
