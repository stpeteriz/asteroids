import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)
        
        
    def update(self,dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_velocity_1 = self.velocity.rotate(random_angle)*1.2
            new_velocity_2 = self.velocity.rotate(-random_angle)*1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_position = self.position.copy()
            asteroid1 = Asteroid(new_position.x,new_position.y,new_radius)
            asteroid1.velocity = new_velocity_1
            asteroid2 = Asteroid(new_position.x,new_position.y,new_radius)
            asteroid2.velocity = new_velocity_2