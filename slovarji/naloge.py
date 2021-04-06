# Naloge s slovarji
# Družinski piknik. Zanima nas, kaaj bodo jedli gostje
# 
# Goste predstavimo s slovarjem: ime -> najljubšo jed

gosti = {"Filip": "musaka", "Miha": "cevapcici"} 
gosti2 = {"Filip": "jabolcn pita", "Luka": "jota"}

# 1. Naloga: iz slovarja gostov vrni seznam vseh gostov
def imena_gostov(s):
    ret = []
    for k in s:
        ret.append(k)
    return ret
print(imena_gostov(gosti)== ["Filip", "Miha"])


# 2. Naloga: Združi slovarja
# Vrne zdruzen slovar,
# kjer so vrednosti podvojene, jih vzame iz s1
def zdruzi(s1, s2):
    ret = {}
    for k in s1:
        ret[k] = s1[k]
    for k in s2:
        if k not in ret:
            ret[k] = s2[k]
    return ret
print(zdruzi(gosti, gosti2) == {"Filip": "musaka", "Miha": "cevapcici", "Luka": "jota"})

# 3. Naloga Izlušči
# Dobimo slovar kaj gostje jedo in ljudi, ki so potrdili udeležbo
# Naredi nakupovalni seznam
# izlusci(gosti, ["Miha", "Filip", "Luka"]) 
#       -> {"musaka": 1, "Cevapcici": 1}
# vrne kolicino potrebnega materiala
def izlusci(slovar, seznam_imen):
    ret = {}
    for ime in seznam_imen:
        if ime in slovar:
            if slovar[ime] in ret:
                ret[slovar[ime]] += 1
            else:
                ret[slovar[ime]] = 1
    return ret
print(izlusci(gosti, ["Filip", "Miha", "Luka"]) == {"musaka" : 1, "cevapcici" : 1})

#4. naloga preveri, ali sta slovarja enaka
def enaka(s1, s2):
    if len(s1) != len(s2):
        return false
    for k, v in s1:
        if s2[k] != v:
            return false
    return true

# 5. naloga sifriraj
nasa_sifra = {'Č': 'K', 'A': 'O', 'C': 'Z', 'B': 'M', 'E': 'V',
'D': 'C', 'G': 'P', 'F': 'E', 'I': 'B', 'H': 'F',
'K': 'I', 'J': 'A', 'M': 'U', 'L': 'H', 'O': 'R',
'N': 'Š', 'P': 'J', 'S': 'T', 'R': 'L', 'U': 'G',
'T': 'Č', 'V': 'N', 'Z': 'Ž', 'Š': 'S', 'Ž': 'D'}

beseda = "JABOLKO"

def zasifriraj(sifra, beseda):
    nova_beseda = ""
    for znak in beseda:
        nova_beseda += sifra[znak]
    return nova_beseda

#6. naloga odsifriraj
sifrirana_beseda = zasifriraj(nasa_sifra,beseda)

def obrni_sifro(sifra):
    nova_sifra = {}
    for k in sifra:
        nova_sifra[sifra[k]] = k
    return nova_sifra

def odsifriraj(sifra, beseda):
    obrnjena_sifra = obrni_sifro(sifra)
    prava_beseda = ""
    for znak in beseda:
        prava_beseda += obrnjena_sifra[znak]
    return prava_beseda

print(odsifriraj(nasa_sifra, zasifriraj(nasa_sifra, beseda)) == beseda)

# 7. naloga preveri ali je slovar sifra, vsak znak se preslika v natancno enega, vsi znaki se preslikajo
