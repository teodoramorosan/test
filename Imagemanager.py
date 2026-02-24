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
            print("1. Încarcă imagine")
            print("2. Info imagine")
            print("3. Redimensionează")
            print("4. Grayscale")
            print("5. Decupează")
            print("6. Salvează")
            print("7. Istoric")
            print("8. Ieșire")

            opt = input("Alege opțiunea: ")

        if opt == "1":
            path = input("Cale imagine:")
            manager.incarca_imagine(path)

        elif opt == "2":
            manager.info_imagine()

        elif opt == "3":
        l = int(input("Lățime nouă:"))
        h = int(input("Înălțime nouă:"))
        manager.redimensioneaza(l, h)

        elif opt =="4":
            manager.grayscale()

        elif opt  == "5":
            s = int(input("Stânga: "))
            j = int(input("Sus: "))
            d = int(input("Dreapta:"))
            jos = int(input("Jos: "))
            manager.decupeaza(s, j, d, jos)

        elif opt == "6":
            nume = input("Nume fișier nou ("ex: editat.jpg): ")
            manager.salveaza(nume)

        elif opt =="7":
            manager.arata_istoric()

        elif opt =="8":
            print("La revedere!")
            break
            
        else:
            print("Optiune invalidă!")


if __name__ == "__main__":
    meniu()