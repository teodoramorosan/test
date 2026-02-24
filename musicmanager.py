from datetime import date
import json
import os

class Melodie:
    def __init__(self, titlu, artist, gen, durata):
        self.titlu = titlu
        self.artist = artist
        self.gen = gen
        self.durata = durata 
    def to_dict(self):
        return{
            "titlu": self.titlu,
            "artist": self.artist,
            "gen": self.gen,
            "durata": self.durata
        }
    
    @staticmethod
    def from_dict(data):
        return Melodie(data["titlu"], data["artist"], data["gen"], data["durata"])
    
    def __str__(self):
        return f"{self.titlu} - {self.artist} | Gen: {self.gen} | {self.durata} min"
    

class MusiManager:
    def __init__(self):
        self.melodii = []

    def adauga_melodie(self):
        titlu = input("Titlu melodie:")
        artist = input("Artist: ")
        gen = input("Gen muzical: ")
        durata = float(input("Durata (minute): "))
    
        melodie = Melodie(titlu, artist, gen, durata)
        self.melodii.append(melodie)
        print("Melodie aăugată cu succes!\n")

    def afiseaza_melodii(self):
        if not self.melodii:
            print("Nu există melodii.\n")
            return
        
        print("\nLista melodii: ")
        for i, moelodie in enumerate(self.melodii, 1):
            print(f"{i}. {melodie}")
        print()

    def cauta_dupa_artist(self):
        nume = input("Introdu numele artistului: ").lower()
        gasite = [m for m in self.melodii if nume in m.artist.lower()]

        if gasite:
            print("\nMelodii găsite:")
            for melodie in gasite:
                print(melodie)
        else:
            print("Nu s-au găsit melodii.\n")
            return
        
        sortate = sorted(sel.melodii, key=lambda m: m.durata, reverse=True)
        print("\nTop melodii cele mai lungi:")
        for melodie in sortate[:3]:
            print(melodie)
        print()

    def salveaza_fisier(self, nume_fisier="melodii.json"):
        with open(nume_fisier, "w") as f:
            json.dump([m.to_dict() for m in self.melodii], f, indent=4)
        print("Date salvate cu succes!\n")

    def incarca_fisier(self, nume_fisier="melodii.json"):
        if not os.path.exists(nume_fisier):
            print("Fișierul nu există.\n")
            return
        
        with open(nume_fisier, "r") as f:
            data = json.load(f)
            self.melodii = [Melodie.from_dict(m) for m in data]
        print("Date încărcate cu succes!\n")



def meniu():
    manager = MusiManager()
    manager.incarca_fisier()

    while True:
        print("===== MUSIC MANAGER =====")
        print("1. Adaugă melodie")
        print("2. Afișează melodii")
        print("3. Caută după artist")
        print("4. Top melodii lungi")
        print("5. Salvează")
        print("6. Ieșire")

        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            manager.adauga_melodie()
        elif optiune == "2":
            manager.afiseaza_melodii()
        elif optiune == "3":
            manager.cauta_dupa_artist()
        elif optiune == "4":
            manager.top_melodii_lungi()
        elif optiune == "5":
            manager.salveaza_fisier()
        elif optiune == "6":
            manager.salveaza_fisier()
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.\n")
        

if __name__ == "__main__":
    meniu()