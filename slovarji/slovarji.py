moj_slovar = {
    1: "Miha",
    2: "Luka",
    3: "Anja",
    4: "Mateja",
    17: "Katarina"
}

moj_slovar[4] = "Francka"

print(moj_slovar[17])
print(moj_slovar[4])

moj_slovar[-3] = "Janez"

print(moj_slovar[-3])

print(14 in moj_slovar)
print(17 in moj_slovar)

print(moj_slovar)

# v while zanki uporabnika sprasuje po sifri in imenu izdelka
# to si shranjuje v nek slovar
# to pocne dokler ni sifra negativna
# ko je negativna nehajte in izpisite cel slovar

hrana = {}

sifra = int(input("Vnesi sifro izdelka. "))

while sifra >= 0:
    hrana[sifra] = input("Vnesi ime izdelka. ")
    sifra = int(input("Vnesi sifro izdelka. "))

print(hrana)

