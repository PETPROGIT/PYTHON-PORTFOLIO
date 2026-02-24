import numpy as np
from camera import Camera
from sphere import Sphere
from light import Light
from renderer import Renderer
from utils import save_image, ensure_output_dir
import random

def random_sphere():
    x = random.uniform(-3, 3)
    y = random.uniform(-2, 3)
    z = random.uniform(-8, -4)
    radius = random.uniform(0.4, 1.2)
    color = [
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0),
        random.uniform(0.3, 1.0)
    ]
    return Sphere([x, y, z], radius, color)

def main():
    spheres = []
    for _ in range(10):
        spheres.append(random_sphere())
    
    spheres.append(Sphere([0, -10, -5], 9.0, [0.6, 0.6, 0.6]))
    
    light = Light(position=[4, 6, -2], intensity=1.5, color=[1.0, 1.0, 1.0])

    camera = Camera(
        position=[0, 1, 5],
        look_at=[0, 0, -5],
        up=[0, 1, 0],
        fov=60,
        aspect_ratio=800/600
    )

    renderer = Renderer(camera, spheres, light, background_color=[0.2, 0.2, 0.4])

    width, height = 800, 800
    print("Рендеринг начат")
    image = renderer.render(width, height)
    print("Рендеринг завершён")

    out_dir = ensure_output_dir()
    save_image(image, f"{out_dir}/output.png")

if __name__ == "__main__":
    main()