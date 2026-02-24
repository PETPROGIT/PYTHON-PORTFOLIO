import numpy as np
from PIL import Image
import os

def save_image(image_array, filename):
    image_array = np.clip(image_array * 255, 0, 255).astype(np.uint8)
    img = Image.fromarray(image_array, 'RGB')
    img.save(filename)
    print(f"Изображение сохранено как {filename}")

def ensure_output_dir(dir_name="output"):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name