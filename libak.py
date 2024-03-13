# ALPROGRAMOK #

def beker():
    l=[]
    with open("libak.txt", "r", encoding="UTF-8") as fm:
        for sor in fm:
            l.append(int(sor.strip()))
    return l

def osszegzes(l):
    szum=0
    for szam in l:
        if szam<=3:
            szum+=szam
    return szum

def kiir(l, rmog):
    print(f"A libák súlyai: {l}")
    print(f"{rmog}kg libát ehet meg a róka.")

# FőPROGRAM #
#Input
libak=beker()
#Számítás
r_megehet_ossz_kg=osszegzes(libak)
#Output
kiir(libak, r_megehet_ossz_kg)