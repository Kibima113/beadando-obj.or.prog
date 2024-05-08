from datetime import date, datetime
from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def foglalhato(self, datum):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

    def foglalhato(self, datum):
        # foglalhatósági ellenőrzés
        return datum > date.today()

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 20000)

    def foglalhato(self, datum):
        # foglalhatósági ellenőrzés
        return datum > date.today()

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if szoba.foglalhato(datum):
                    foglalas = Foglalas(szoba, datum)
                    self.foglalasok.append(foglalas)
                    print(f"Sikeres foglalás! Ár: {szoba.ar}")
                    return foglalas
                else:
                    print("A megadott szoba nem foglalható ezen a dátumon vagy nem létezik. Kérlek válaszd ki a szobát az elérhető szobákból és dátumokból")
                    return None
        print("A megadott szoba nem létezik.")

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print("Foglalás sikeresen törölve.")
        else:
            print("Nincs ilyen foglalás.")

    def listazas(self):
        print("Összes foglalás:")
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

# Szálloda, szobák és foglalások létrehozása
szalloda = Szalloda("Példa Szálloda")
szalloda.uj_szoba(EgyagyasSzoba("101"))
szalloda.uj_szoba(EgyagyasSzoba("102"))
szalloda.uj_szoba(EgyagyasSzoba("103"))
szalloda.uj_szoba(EgyagyasSzoba("104"))
szalloda.uj_szoba(KetagyasSzoba("201"))
szalloda.uj_szoba(KetagyasSzoba("202"))
szalloda.uj_szoba(KetagyasSzoba("203"))
szalloda.uj_szoba(KetagyasSzoba("204"))

# néhány foglalás
foglalasok = [
    szalloda.foglalas("101", date(2024, 5, 10)),
    szalloda.foglalas("102", date(2024, 5, 11)),
    szalloda.foglalas("201", date(2024, 5, 12)),
    szalloda.foglalas("101", date(2024, 5, 13)),
    szalloda.foglalas("201", date(2024, 5, 14)),
    szalloda.foglalas("103", date(2024, 5, 10)),  
    szalloda.foglalas("104", date(2024, 5, 11)),  
    szalloda.foglalas("202", date(2024, 5, 12)),  
    szalloda.foglalas("102", date(2024, 5, 13)),  
    szalloda.foglalas("203", date(2024, 5, 14))   
]

# Felhasználói interakció
while True:
    print("\n1 - Foglalás")
    print("2 - Lemondás")
    print("3 - Foglalások listázása")
    print("0 - Kilépés")
    valasztas = input("Válassz egy műveletet: ")

    if valasztas == "1":
        szobaszam = input("Add meg a szoba számát: ")
        datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            szalloda.foglalas(szobaszam, datum)
        except ValueError:
            print("Hibás dátumformátum!")
    elif valasztas == "2":
        szobaszam = input("Add meg a szoba számát: ")
        datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            szalloda.lemondas(szobaszam, datum)
        except ValueError:
            print("Hibás dátumformátum!")
    elif valasztas == "3":
        szalloda.listazas()
    elif valasztas == "0":
        break
    else:
        print("Érvénytelen választás!")
