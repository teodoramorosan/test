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