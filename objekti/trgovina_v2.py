

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

    def stevilo_razlicnih_izdelkov(self):
        stevilo = 0
        for izdelek in self.zaloga:
            pr = izdelek[1]
            if pr.kolicina > 0:
                stevilo += 1
        return stevilo

#napisi se ostale metode za trgovino

    def skupna_masa_trgovine(self):
        skupna = 0
        for id_izdelka, pr in self.zaloga:
            skupna += izdelek.skupna_masa()
        return skupna


    def vrednost_vse_trgovine(self):
        skupna = 0
        for izdelek in sef.zaloga:
            skupna +=  izdelek[1].skupna_vrednost()
        return skupna

    def st_vseh_izdelkov(self):
        skupna = 0
        for izdelek in self.zaloga:
            skupna +=  izdelek[1].kolicina
        return skupna


    def izdelek_z_najvisjo_vrednostjo(self):
        najvisja = self.zaloga[0][1]
        for element in self.zaloga:
            if element[1].skupna_vrednost() > najvisja.skupna_vrednost():
                najvisja = element[1]
        return najvisja

# neki naj vrne vrednost vse hrane
# neki naj vrne vrednost vse pijace
    
# dodaj funkcijo kupi(self, id_izdelka, spremeba_kolicine)
# funkcija naj se spehodi po zalogi (self.zaloga)
# najde izdelek s pravim id-jem in popravi njegovo zalogo
# naj vrne true, ko ga najde in uspesno popravi zalogo
# popravljanje zaloge: pr.kolicina -= spremeba_kolicine

    def kupi(self, id_izdelka, sprememba_kolicine):
        for izdelek in self.zaloga:
            if izdelek[0] == id_izdelek:
                if izdelek[1].kolicina >= sprememba_kolicine:
                    izdelek[1].kolicina -= sprememba_kolicine
                    return true
                return false

    def dostopni_izdelki(self):
        ret = []
        for id_izdelka, pr in self.zaloga:
            if pr.kolicina > 0:
                ret.append(id_izdelka)

jabolko = Produkt(1.2, 12, "Jabolka", 5, True)
banana = Produkt(0.8, 12, "Banane", 0.4, True)
kruh = Produkt(0.9, 12, "Kruh", 0.5, True)
rizev_napitek = Produkt(1.1, 12, "Rizev napitek", 1, False)
moka = Produkt(2.1, 12, "moka", 1, True)
cokoladni_namaz = Produkt(1.8, 12, "Cokoladni namaz", 0.2, True)
jabolcni_sok = Produkt(1.4, 12, "Jabolcni sok", 1, False)

trgovina = [jabolko, banana, kruh, rizev_napitek, moka, cokoladni_namaz, jabolcni_sok]
trgovina_objekt = Trgovina(trgovina)

"""
Kaj je to?

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


# while zanka: uporabniku naj izpise id-je izdelkov v trgovini,
# ga vprasa za id in kolicino
# in nakupi ta izdelek
# dokler ne vpise id-ja -1

hoce_izdelke = True

while hoce_izdelke:
    print("Na zalogi imamo izdelke z id-ji:")
    print(trgovina_objekt.dostopni_izdelki()) #to je zelo grdo ampak kaj cmo
    zahteva = int(input("Kateri izdelek zelis? Ce ne zelis izdelka vnesi -1. "))
    if zahteva == -1:
        hoce_izdelke = False
    elif not trgovina_objekt.kupi(zahteva,int(input("koliko izdelka zelis? "))):
        print("Nakup zal ni uspel, poskusite, kaj drugega.")

