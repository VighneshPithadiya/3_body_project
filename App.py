import pygame

class App: #controls the pygame things 
    def __init__(self, width = 800, height = 600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height)) 
        pygame.display.set_caption("3-Body Simulation")
        self.clock = pygame.time.Clock()
        self.running = True #determines if the pygame keeps running
        self.simulation = None #will be set later

    def set_simulation(self, simulation):
        self.simulation = simulation
    
    def run(self):
        while self.running:       
            self.simulation.update() #updates the positions and velocities of all bodies
            self.screen.fill((0, 0, 0))

            for body in self.simulation.bodies:
                body.draw(self.screen) 
            
            pygame.display.flip()

            self.clock.tick(60) #limit to 60 FPS

            #allows window to be closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            