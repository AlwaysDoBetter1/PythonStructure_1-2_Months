'''
A clear example of the Monte Carlo method Python

In this example, we generate a large number of random points within a unit square (with sides of length 1).
We then check if each point falls within the unit circle (centered at the origin). If the point's distance
from the origin is less than or equal to 1 (which means it's inside the unit circle), we count it as inside
the circle. Finally, we estimate the value of π by taking the ratio of points inside the circle to the total
number of points generated and multiplying by 4. The more points we generate, the closer our estimate will
be to the actual value of π.
'''

import random

def estimate_pi(num_points):
    inside_circle = 0
    total_points = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
        total_points += 1

    pi_estimate = 4 * inside_circle / total_points
    return pi_estimate

# Number of points to generate
num_points = 1000000

# Estimate pi
pi_estimate = estimate_pi(num_points)
print("Estimated value of pi:", pi_estimate)

