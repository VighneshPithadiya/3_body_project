import pygame
import numpy as np

class Body:
    def __init__(self, position, velocity, color, mass, radius = 5):
        self.position = np.array(position, dtype=float) #a list of x, y coordinates
        self.velocity = np.array(velocity, dtype=float) # a list of x, y velocity components 
        self.color = color
        self.radius = radius
        self.mass = mass
        self.history = [] #to draw trajectory trails (maybe)

    def update_position(self, dt):
        np.add(self.position, self.velocity * dt, out=self.position)
        self.history.append(tuple(self.position.tolist())) #store position as a tuple for drawing trails
        if len(self.history) > 200:
            self.history.pop(0) # Limit history length, remove oldest
    
    def draw(self, screen):
        position = self.position.tolist() 
        x, y = int(position[0]), int(position[1])
        pygame.draw.circle(screen, self.color, (x, y), self.radius)
        # if len(self.history) > 1:
        #     pygame.draw.lines(screen, self.color, closed = False, points = self.history, width = 2) #draws multiple connected lines throuhgout the different points in self.history
    
      
