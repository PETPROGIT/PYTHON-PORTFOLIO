import numpy as np

class Vector3:
    def __init__(self, x, y, z):
        self.data = np.array([x, y, z], dtype=float)

    def __add__(self, other):
        return Vector3(*(self.data + other.data))

    def __sub__(self, other):
        return Vector3(*(self.data - other.data))

    def __mul__(self, scalar):
        return Vector3(*(self.data * scalar))

    def dot(self, other):
        return np.dot(self.data, other.data)

    def norm(self):
        return np.linalg.norm(self.data)

    def normalize(self):
        return self * (1.0 / self.norm())

    def to_array(self):
        return self.data