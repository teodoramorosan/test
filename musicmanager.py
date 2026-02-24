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

    def incarca_fisier(self, nume_fisier"melodii.jason")