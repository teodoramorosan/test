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
    def sterge_carte(self):
        self.afiseaza_carti()
        try:
            index = int(input("Număr carte de șters:"))
            if 0 <= index < len(self.carti):
                del self.carti[index]
                self.save_data()
                print("✔ Carte adăugată cu succes!")
    
    def afiseaza_carti(self):
        if not self.carti:
            print("Nu există cărți în bibliotecă.")
            return
        
        for i, carte in enumerate(self.carti,1):
            status = "Disponibilă"
            if carte.imprumutata:
                status = f"Împrumutată de {carte.imprumutata_de}"
            print(f"{i}. {carte.titlu} - {carte.autor} ({carte.an}) | {status})")

    def sterge_carte(self):
        self.afiseaza_carti()
        try:
            index = int(input("Număr carte de șters: ")) - 1
            if 0 <= index < len(self.carti):
                del self.carti[index]
                self.save_data()
                print("✔ Carte ștearsă!")
            else:
                print("Index invalid!")
        except:
            print("Input invalid!")

    def imprumutata_carte(self, utilizator):
        self.afiseaza_carti()
        try:
            index = int(input("Număr carte de împrumuta: ")) - 1
            if 0 <= index < len(self.carti):
                carte = self.carti[index]
                if not carte.imprumutata:
                    carte.imprumutata = True
                    carte.imprumutata_de = utilizator
                    carte.data_imprumut = datetime.now().strftime("%Y-%m-%d")
                    self.save_data()
                    print("✔ Carte împrumutată!")
                else:
                    print("Cartea este deja împrumutată.")
            else:
                print("Index invalid!")
        except:
            print("Input invalid!")
        
        def returneaza_carte(self,utilizator):
            carti_utilizator = [c for c in self.carti if c.imprumutata_de == utilizator]

            if not carti_utilizator:
                print("Nu ai cărți împrumutate.")
                return

            for i, carte in enumerate(carti_utilizator, 1):
                print(f"{i}. {carte.titlu}")
            
            try:
                index = int(input("Număr carte de returnat:")) - 1
                if 0 <= index < len(carti_utilizator):
                    carte = carti_utiliator[index]
                    carte.imprumutata = False
                    carte.imprumutata_de = None
                    carte.data_imprumut = None
                    self.save_data ()
                    print("✔ Carte returnată!")
                else:
                    print("Index invalid!")
            except:
                print("Input invalid!")

        def cauta_carte(self):
            termen = input("Introdu titlu sau autor:").lower()
            rezultate = [c for c in self.carti if termen in c.titlu.lower() or termen in c.autor.lower()]

            if rezultate:
                for carte in rezultate:
                    print(f"{carte.titlu} - {carte.autor} ({carte.an})")
                else:
                    print("Nici o carte găsită.")

        def inregistreaza_utilizator(self):
            username = input ("Username nou: ")
            if username in self.utilizatori:
                print ("Utilizator existent!")
                return
            parola = input("Parola: ")
            self.utilizator[username] = parola
            self.save_data()
            print("✔ Utilizator creat!")

        def login(self):
            username = input("Username: ")
            parola = input("Parola: ")
            if self.utilizatori.get(username) == parola:
                print("✔ Autentificare reușită!")
                return username
            else:
                print("Date incorecte!")
                return None
        

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== SISTEM BIBLIOTECĂ ===")
        print("1. Login")
        print("2. Înregistrare")  
        print("3. Ieșire")
    
        alegere = input("Alege opțiunea: ")

        if alegere == "1":
            user = biblioteca.login()
            if user:
                while True:
                    print(f"\n--- Meniu utilizator ({user}) ---")
                    print("1. Afișează cărți")
                    print("2. Adaugă carte")
                    print("3. Șterge carte")
                    print("4. Împrumută carte")
                    print("5. Returnează carte")
                    print("6. Caută carte")
                    print("7. Logout")

                    opt = input("Alege: ")

                    if opt == "1":
                        biblioteca.afiseaza_carti()
                    elif opt == "2":
                        biblioteca.adauga_carte()
                    elif opt == "3":
                        biblioteca.sterge_carte()
                    elif opt == "4":
                        biblioteca.imprumutata_carte(user)
                    elif opt == "5":
                        biblioteca returneaza_carte(user)
                    elif opt == "6":
                        biblioteca.cauta_carte()
                    elif opt == "7":
                        break
                    else:
                        print("Opțiune invalidă!")

            elif alegere == "2":
                biblioteca.inregistreaza_utilizator()
            elif alegere == "3":
                print("La revedere!")
                break
            else:
                print("Opțiune invalidă!")


if  __name__ == "__main__":
    main()