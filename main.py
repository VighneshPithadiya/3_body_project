from Body import Body
from Simulation import Simulation
import pygame

b1 = Body(position = [400, 600], velocity = [0, 0], color = (255, 0, 0), mass = 100, radius = 8)
b2 = Body(position = [400, 400], velocity = [0, 0], color = (0, 255, 0), mass = 200, radius = 6)
b3 = Body(position = [200, 600], velocity = [0, 0], color = (0, 0, 255), mass = 300, radius = 5)

sim =  Simulation(bodies = [b1, b2, b3])

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3-Body Simulation")
clock = pygame.time.Clock()
running = True

while running:
    sim.update()
    screen.fill((0, 0, 0))
    
    for body in sim.bodies:
        body.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()