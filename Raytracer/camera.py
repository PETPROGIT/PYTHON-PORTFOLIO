import numpy as np
from ray import Ray

class Camera:
    def __init__(self, position, look_at, up, fov, aspect_ratio):
        self.position = np.array(position, dtype=float)
        self.look_at = np.array(look_at, dtype=float)
        self.up = np.array(up, dtype=float)
        self.fov = fov
        self.aspect_ratio = aspect_ratio

        self.forward = (self.look_at - self.position)
        self.forward = self.forward / np.linalg.norm(self.forward)
        self.right = np.cross(self.forward, self.up)
        self.right = self.right / np.linalg.norm(self.right)
        self.up = np.cross(self.right, self.forward)

    def get_ray(self, u, v):
        half_height = np.tan(np.radians(self.fov) / 2)
        half_width = half_height * self.aspect_ratio

        dir = self.forward + (u - 0.5) * 2 * half_width * self.right - (v - 0.5) * 2 * half_height * self.up
        return Ray(self.position, dir)