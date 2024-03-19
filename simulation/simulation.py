import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera
# from IPython.display import HTML


class Robot:
    def __init__(self, x, y, cable_length=None):
        self.pos = np.array([x, y]).astype(float)
        self.vel = np.array([0.0, 0.0]).astype(float)
        self.cable_length = cable_length

    def apply_force(self, force):
        self.vel += force

    def update_position(self, dt):
        self.pos += self.vel * dt

    def check_cable_constraint(self, central_robot):
        distance = np.linalg.norm(self.pos - central_robot.pos)
        if distance > self.cable_length:
            direction = (self.pos - central_robot.pos) / distance
            overflow = distance - self.cable_length
            self.pos -= direction * overflow


# Initialize central and peripheral robots
central_robot = Robot(0, 0)

n = 5  # Number of peripheral robots
peripheral_robots = [Robot(np.cos(2 * np.pi * i / n) * 10., np.sin(2 * np.pi * i / n) * 10., 10) for i in range(n)]

# Time step and simulation time
dt = 0.1
T = 10.0

# Initialize plot
# plt.ion()
fig, ax = plt.subplots()
camera = Camera(fig)

# Simulation loop
for t in np.arange(0, T, dt):
    #     ax.clear()
    sum_forces = np.array([0.0, 0.0])

    # Update each peripheral robot
    for robot in peripheral_robots:
        # Apply random force
        force = np.random.uniform(-1, 1, 2)
        robot.apply_force(force)

        # Update position
        robot.update_position(dt)

        # Check cable constraint
        robot.check_cable_constraint(central_robot)

        # Add the force to the sum of forces acting on the central robot
        sum_forces += force

        # Plot
        ax.plot([central_robot.pos[0], robot.pos[0]], [central_robot.pos[1], robot.pos[1]], 'ro-')

    central_robot.apply_force(sum_forces)
    central_robot.update_position(dt)
    # Plot central robot
    ax.plot(central_robot.pos[0], central_robot.pos[1], 'go')

    ax.set_aspect('equal')

    camera.snap()