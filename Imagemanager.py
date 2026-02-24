from email.mime import image

from PIL import Image
import os
from datetime import datetime

class ImageManager:
    def __init__(self):
        self.current_image = None
        self.image_path = None
        self.history = []

    def incarca_imagine(self, path):
        if not os.path.exists(path):
            print("Imaginea nu există!")
            return
        
        sellf.current_image = Image.open(path)
        self.image_path = path
        self.history.append(f"")