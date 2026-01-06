# 3-Body Problem Simulation

## Overview

This project simulates the three-body problem, a classic challenge in classical mechanics and astrophysics. The three-body problem involves predicting the motions of three mutually attracting celestial bodies under the influence of Newton's law of universal gravitation. Unlike the two-body problem, which has an analytical solution, the three-body problem is generally chaotic and does not have a closed-form solution, making numerical simulation essential.

## The Three-Body Problem

In the three-body problem, three point masses interact gravitationally. The system is governed by Newton's laws of motion and the law of universal gravitation:

\[ F = G \frac{m_1 m_2}{r^2} \]

Where:
- \( F \) is the gravitational force
- \( G \) is the gravitational constant
- \( m_1, m_2 \) are the masses
- \( r \) is the distance between the bodies

The complexity arises because each body's motion affects the others, leading to chaotic behavior where small changes in initial conditions can result in vastly different outcomes.

## Simulation Implementation

This simulation uses a numerical approach to approximate the solution:

### Key Components

- **Body.py**: Defines the `Body` class representing celestial bodies with position, velocity, mass, and visual properties.
- **Simulation.py**: Contains the `Simulation` class that manages the physics calculations and updates.
- **main.py**: Sets up the initial conditions and runs the Pygame-based visualization.

### Physics Engine

The simulation employs the Euler integration method for numerical integration:

1. Calculate gravitational accelerations for each body due to the others
2. Update velocities: \( \vec{v} = \vec{v} + \vec{a} \cdot dt \)
3. Update positions: \( \vec{r} = \vec{r} + \vec{v} \cdot dt \)

Where \( dt \) is the time step (default 0.01).

### Visualization

The simulation uses Pygame to render the bodies as colored circles on a 2D canvas. The frame rate is capped at 1 FPS to allow observation of the motion.

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
- Body 1: Mass 10000, Position (400, 300), Velocity (0, 0), Red
- Body 2: Mass 20000, Position (400, 100), Velocity (150, 0), Green
- Body 3: Mass 30000, Position (200, 300), Velocity (0, -120), Blue

## Customization

You can modify initial conditions in `main.py` or adjust parameters like gravitational constant `G` and time step `dt` in `Simulation.py` to explore different scenarios.

## Limitations

- Uses simple Euler integration, which can accumulate errors over time
- 2D simulation (no z-axis)
- No collision detection
- Chaotic nature means long-term predictions may diverge

For more accurate simulations, consider using more advanced integration methods like Runge-Kutta or symplectic integrators.