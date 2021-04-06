# print(chr(95))
# print(ord("A"))

# napisi funkcijo, kjer clovek poda ime in priimek funkcija pa vrne vsoto znakov
slovar_grdih_crk = {'č':'c', 'š':'s', 'ž':'z'}
crke = {}
a = ord('a')
z = ord('z')
for znak in 'qwertyuiopasdfghjklzxcvbnm':
    crke[znak] = ord(znak) - a

def vsota_znakov(niz):
    vsota = 0
    for znak in niz.lower():
        if znak != ' ' and znak != '-' and znak != "'":
            if znak in slovar_grdih_crk:
                vsota += crke[slovar_grdih_crk[znak]] - a
            else:
                vsota += crke[znak] - a
    return vsota

# cezar
abeceda = 'abcdefghijklmnopqrstuvwxyz'
dolzina_abeceda = len(abeceda)

def zasifriraj(beseda, kljuc):
    ret = ''
    for znak in beseda.lower():
        ret +=abeceda[(crke[znak] + kljuc) % dolzina_abecede]
    return ret

def odsifriraj(beseda, kljuc):
    return zasifriraj(beseda, 26-kljuc)

# sifriraj/odsifriraj besedilo s presledki
def sifriraj_znak(znak, k):
    return abeceda[(crke[znak] + kljuc) % dolzina_abecede]

def dezifriraj_znak(znak, k):
    return sifriraj_znak(znak, dolzina_abecede - k)

def sifriraj_besedilo(besedilo, kljuc):
    novo_besedilo = ''
    for znak in besedilo:
        if znak in abeceda:
            if znak.lower() == znak:
                novo_besedilo.append(sifriraj_znak(znak, kljuc))
            else:
                novo_besedilo.append(sifriraj_znak(znak.lower(), kljuc).upper())
    return novo_besedilo

def odsifriraj_besedilo(besedilo, kljuc):
    return sifriraj_besedilo(besedilo, dolzina_abecede - kljuc)

for i in range(26):
    print(zasifriraj('abcdefghijklmnopqrstuvwxyz', i))


























