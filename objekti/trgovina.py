

class Produkt:
    # Cena je na enoto kolicine
    # masa je na enoto kolicine v kg
    def __init__(self, cena, kolicina, ime, masa, je_hrana):
        self.cena = cena
        self.kolicina = kolicina
        self.ime = ime
        self.masa = float(masa)
        self.je_hrana = je_hrana

    def skupna_masa(self):
       return self.masa * self.kolicina
    
    def izracunaj_stopnjo_davka(self):
        if self.je_hrana:
            return 0.095
        return 0.22

    def skupna_vrednost(self):
        return self.kolicina * self.cena * (1 + izracunaj_stopnjo_davka(self))

class Trgovina:
    def __init_(self, zaloga):
        zacetna_sifra = 0
        zaloga_trgovine = []
        for pr in zaloga:
            zaloga_trgovine.append((zacetna_sifra, pr))
            zacetna_sifra += 1
        self.zaloga = zaloga_trgovine

jabolko = Produkt(1.2, 12, "Jabolka", 5, True)
trgovina = [jabolko]
trgovina.append(Produkt(0.8, 12, "Banane", 0.4, True))
trgovina.append(Produkt(0.9, 12, "Kruh", 0.5, True))
trgovina.append(Produkt(1.1, 12, "Rizev napitek", 1, False))
trgovina.append(Produkt(2.1, 12, "Semolina flour", 1, True))
trgovina.append(Produkt(1.8, 12, "Cokoladni namaz", 0.2, True))
trgovina.append(Produkt(1.4, 12, "Jabolcni sok", 1, False))

trgovinaC = Trgovina(trgovina)

def skupna_teza_trgovine(seznam):
    skupna = 0
    for izdelek in seznam:
        skupna += izdelek.skupna_masa()
    return skupna

def vrednost_vse_trgovine(seznam):
    skupna = 0
    for izdelek in seznam:
        skupna +=  izdelek.skupna_vrednost()

def st_vseh_izdelkov(seznam):
    skupna = 0
    for izdelek in seznam:
        skupna +=  izdelek.kolicina

def najvisja_vrednost(seznam):
    najvisja = seznam[0]
    for elementInd in range(1, len(seznam)):
        if element.skupna_vrednost() > najvisja.skupna_vrednost():
            najvisja = element
    return najvisja
"""
def najdrazji_nadef vrednost_vse_trgovine(seznam):
    skupna = 0
    for izdelek in seznam:
        skupna +=  izdelek.skupna_vrednost()
enoto(seznama):
    najdrazji = seznam[0]
    for element in seznam:
        if element.cena*najdrazji.masa > najdrazji.cena*element.masa:
            najdrazji = element
    return najdrazji

"""

#napisi 3 fje
    #vrni vredost vse trgovine
    #vrni st vseh iydelkov
    #vrni izdelek z najvisjo vrednostjo
#kateri izdelek je na enoto  kol-vo najdrazji
#poracunaj skupno vrednost hrane in skpuno vrednost pijace
