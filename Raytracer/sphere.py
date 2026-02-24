import numpy as np

class Sphere:
    def __init__(self, center, radius, color):
        self.center = np.array(center, dtype=float)
        self.radius = radius
        self.color = np.array(color, dtype=float)

    def intersect(self, ray):
        oc = ray.origin - self.center
        a = np.dot(ray.direction, ray.direction)
        b = 2.0 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None

        sqrt_disc = np.sqrt(discriminant)
        t1 = (-b - sqrt_disc) / (2.0 * a)
        t2 = (-b + sqrt_disc) / (2.0 * a)

        t = None
        if t1 > 1e-4:
            t = t1
        if t2 > 1e-4 and (t is None or t2 < t):
            t = t2

        return t