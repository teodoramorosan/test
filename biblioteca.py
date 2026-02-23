import json
import osfrom datetime import datetime

DATA_FILE = "biblioteca_data.json" 


class Carte:
    def __init__(self, titlu, autor, an):
        self.titlu = titlu
        self.autor = autor
        self.an = an 
        self.imprumutata = False
        self.imprumutata_de = None
        self.data_imprumut = None

    def to_dict(self):
        return self.__dict__
    
    @staticemethod
    def from_dict(data):
        carte = Carte(data["titlu"], data["autor"], data["an"])
        carte.imprumutata = data["imprumutata"]
        carte.imprumutata_de = data["imprumutata_de"]
        carte.data_imprumut = data["data_imprumut"]
        return carte
    

class Biblioteca:
    def __init__(self):
        self.carti = []
        self.utilizatori = {"admin": "admin123"}
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.carti = [Carte.from_dict(c) for c in data.get("carti", [])]
                self.utilizatori = data.get("utilizatori", self.utilizatori)
    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump({
                "carti":[c.to_dict() for c in self.carti],
                "utilizatori": self.utilizatori
            }, f, indent=4)

    def adauga_carte(self):
        titlu = input("Titlu: ")
        autor = input("Autor: ")
        an = input("An aparitie:")
        carte = Carte(titlu, autor, an)
        self.carti.append(carte)
        self.save_data()
        print("✔ Carte adăugată cu succes!")

    def afiseaza_carti(self):
        if not self.carti:
            print("Nu există cărți în bibliotecă.")
            return

        for i, carte in enumerate(self.carti, 1):
            status = "Disponibilă"
            if carte.imprumutata:
                status = f"Împrumutată de {carte.imprumutata_de}"
            print(f"{i}. {carte.titlu} - {carte.autor} ({carte.an}) | {status}")    