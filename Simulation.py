import pygame 
import numpy as np
from Body import Body

class Simulation: #controls the bodies and the physics
    def __init__(self, bodies, G = 10, dt=0.1):
        self.bodies = bodies #list of all Body objects in the simulation
        self.G = G #gravitational constant
        self.dt = dt #time step

    def compute_accelerations(self):
        """ 
        Returns a 2d array of accelerations for each body"""
        accels_of_all_bodies = []
        for current in self.bodies:
            total_acceleration = np.zeros(2) #2D array to hold acceleration vectors
            for other in self.bodies:
                if current is other:
                    continue
                dist = np.sqrt(np.sum((np.subtract(current.position, other.position)) ** 2))  #distance between the two bodies
                if dist < 1e-10:
                    continue
                Force_g = self.G *(current.mass * other.mass) / (dist ** 2) #gravitational force magnitude
                direction_vector = np.subtract(other.position, current.position) / dist #unit vector from current to other
                accel = (Force_g / current.mass) * direction_vector #acceleration vector due to other body
                total_acceleration = np.add(total_acceleration, accel)
            accels_of_all_bodies.append(total_acceleration)
        return accels_of_all_bodies



    def update(self):
        accelerations = self.compute_accelerations()
        for i in range(len(self.bodies)):
            np.add(self.bodies[i].velocity, accelerations[i] * self.dt, out=self.bodies[i].velocity)
            self.bodies[i].update_position(self.dt) 

    