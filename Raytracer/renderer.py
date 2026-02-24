import numpy as np
from ray import Ray

class Renderer:
    def __init__(self, camera, scene_spheres, light, background_color):
        self.camera = camera
        self.scene_spheres = scene_spheres
        self.light = light
        self.background_color = np.array(background_color, dtype=float)

    def trace(self, ray, depth=0):
        closest_t = float('inf')
        closest_sphere = None

        for sphere in self.scene_spheres:
            t = sphere.intersect(ray)
            if t is not None and t < closest_t:
                closest_t = t
                closest_sphere = sphere

        if closest_sphere is None:
            return self.background_color

        hit_point = ray.point_at(closest_t)
        normal = (hit_point - closest_sphere.center) / np.linalg.norm(hit_point - closest_sphere.center)

        surface_color = closest_sphere.color

        light_dir = self.light.position - hit_point
        light_dir = light_dir / np.linalg.norm(light_dir)

        shadow_ray = Ray(hit_point + normal * 1e-4, light_dir)
        in_shadow = False
        for sphere in self.scene_spheres:
            if sphere.intersect(shadow_ray) is not None:
                in_shadow = True
                break

        if in_shadow:
            return surface_color * 0.2 

        diffuse = max(0.0, np.dot(normal, light_dir))
        light_intensity = self.light.intensity * diffuse

        final_color = surface_color * light_intensity * self.light.color

        final_color = np.clip(final_color, 0.0, 1.0)

        return final_color

    def render(self, width, height):
        image = np.zeros((height, width, 3), dtype=float)

        for j in range(height):
            for i in range(width):
                u = i / (width - 1)
                v = j / (height - 1)
                ray = self.camera.get_ray(u, v)
                color = self.trace(ray)
                image[j, i] = color

        return image