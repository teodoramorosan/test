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
        self.history.append(f"{datetimr.now()} - Imagine încărcată")
        print("Imagine încărcată cu succes!")
        
    def info_imagine(self):
        if not self.current_image:
            print("Nu există imagine încărcată!")
            return
        
        print("\n=== INFORMAȚII IMAGINE ===")
        print(f"Format: {self.current_image.format}")
        print(f"Dimensiune: {self.current_image.size}")
        print(f"Mod culoare: {self.current_image.model}")
        print(f"Fișier: {self.image_path}\n")

    def redimensioneaza(self, latime, inaltime):
        if not self.current_image:
            print("Nu există imagine.")
            return
        
        self.current_image = self.current_image.resize((latime, inaltime))
        self.history.append(f"{datetime.now()} - Redimensionată la {latime}x{inaltime}")

    def grayscale(self):
        if not self.current_image:
            print("Nu există imagine.")
            return
        
        self.current_image = self.current_image.convert("L")
        self.history.append(f"{datetime.now()} - Convertită în grayscale")
        print("Imagine convertită în alb-negru!")

    def decupeaza(self, stanga, sus, dreapta, jos):
        if not self.current_image:
            print("Nu există imagine.")
            return
        
        self.current_image = self.current_image.crop((stanga, sus, dreapta, jos))
        self.history.append(f"{datetime.now()} - Decupată
        print("Imagine salvată!")

    def arata_istoric(self):
        print("\n=== ISTORIC MODIFICĂRI ===")
        for actiune in self.history:
            print(actiune)
        print()

    def meniu(self):
        manager = ImageManager()

        while True:
            print("====== IMAGE MANAGER ======")
     