# 3-Body Problem Simulation

## Overview

This project simulates the three-body problem, a well known challenge in the fields of classical mechanics and astrophysics. The three-body problem involves predicting the motion of three mutually attracting celestial bodies under the influence of gravity based on Newton's Universal Law of Gravitation. Unlike the two-body problem that has an analytical solution, the three-body problem is generally chaotic and does not have a closed-form solution, making simulation necessary to understand the potential outcomes

## The Three-Body Problem

In the three-body problem, three point masses interact gravitationally. The system is governed by Newton's laws of motion and the law of universal gravitation:        

F = G*(m_1 * m_2)/r**2

Where:
-  F  is the gravitational force
-  G  is the gravitational constant (6.67 *10^-11)
- m_1, m_2  are the masses
-  r is the distance between the bodies

The complexity arises because each body's motion affects the others, leading to chaotic behavior where even seemingly small and insignficant changes in the initial conditions can result in vastly different outcomes.

### Key Components

- **Body.py**: Defines the `Body` class representing celestial bodies with position and velocity arrays, mass, radius, and color.
- **Simulation.py**: Contains the `Simulation` class that manages the physics calculations and calls for updating positions and velocities.
- **main.py**: Sets up the initial conditions and runs the Pygame-based visualization.

### Physics Engine

The simulation employs the following method to predict motion for each object:

1. Calculate the magnitude of gravity using Newton's Universal Law of Gravitation: F = G*(m_1 * m_2)/r**2
2. Calculate the direction vector of gravity: [x1 - x2, y1- y2]/ distance where [x1, y1] and [x2, y2] are positions of two objects
3. Calculate the acceleration due to gravity: Force_of_gravity/mass * direction_vector 
4. Find acceleration due to gravity exerted by all objects: repeat steps 1-3 for every other body and add the acceleration vectors together
5. Update the velocity: self.velocity + total_acceleration *dt
6. Update the position: self.position + self.velocity where self.velocity is updated due to acceleration

dt is the time step (default 0.01) that essentially determines the speed of the simulation

### Visualization

The simulation uses Pygame to render the bodies as colored circles on a 2D canvas. The time step is set to 0.1 to allow observation of the motion.

## Running the Simulation

### Prerequisites

- Python 3.7+
- Pygame
- NumPy

### Installation

1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install pygame numpy
   ```

### Execution

Run the simulation:
```bash
python main.py
```

A Pygame window will open showing the three bodies in motion.

## Initial Conditions

The simulation starts with three bodies:
- b1 = position = [400, 600], velocity = [0, 0], color = (255, 0, 0), mass = 100, radius = 8
- b2 = position = [400, 400], velocity = [0, 0], color = (0, 255, 0), mass = 200, radius = 6
- b3 = position = [200, 600], velocity = [0, 0], color = (0, 0, 255), mass = 300, radius = 5
## Customization

You can modify initial conditions in `main.py` or adjust parameters like gravitational constant `G` and time step `dt` in `Simulation.py` to explore different scenarios.

## Limitations

- Uses simple calculations, which may result in improper predictions at times
- 2D simulation (no z-axis)
- No collision detection
- Chaotic nature means long-term predictions may diverge

