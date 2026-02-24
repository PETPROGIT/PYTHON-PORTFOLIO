import numpy as np

class Light:
    def __init__(self, position, intensity=1.0, color=None):
        self.position = np.array(position, dtype=float)
        self.intensity = intensity
        if color is None:
            self.color = np.array([1.0, 1.0, 1.0])
        else:
            self.color = np.array(color, dtype=float)