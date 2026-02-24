import numpy as np

class Ray:
    def __init__(self, origin, direction):
        self.origin = np.array(origin, dtype=float)
        self.direction = np.array(direction, dtype=float)
        self.direction = self.direction / np.linalg.norm(self.direction)

    def point_at(self, t):
        return self.origin + t * self.direction