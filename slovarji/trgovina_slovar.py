slovar ={}

sifra = 100
whila sifra > 0:
    sifra = int(input("Vnesi sifro: "))
    ime = input("Vnesi izdelek: ")
    slovar[sifra] = ime

print (slovar)

# to predstavlja mojo zalogo
trgovina = {
        "mleko": 10,
        "jajca": 15,
        "kruh": 7,
}

# tece v while zanki in naredi sledece
# izpise kaj je na voljo v trgovini
# izberi moznost kupi/dodaj/izhod
# potem vpise izdelek n kolicino in ga kupi/doda

moznost = ""

while moznost != "izhod":
    for k in trgovina:
        print(k, trgovina[k])
    moznost = input("kaj zelis narediti? izberi kupi/dodaj/izhod")
    if moznost == 'kupi':
        kolicina = int(input("Koliko?"))

