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

def megszamolas(l):
    db=0
    for suly in l:
        if suly<=3:
            db+=1
    return db

def kiir(l, rmog, ra):
    print(f"A libák súlyai: {l}")
    print(f"{rmog}kg libát ehet meg a róka.")
    print(f"Átlagosan {ra}kg-os libákat eszik a róka.")

# FőPROGRAM #
#Input
libak=beker()
#Számítás
r_megehet_ossz_kg=osszegzes(libak)
r_megehet_db=megszamolas(libak)
r_atlag=r_megehet_db/r_megehet_db
#Output
kiir(libak, r_megehet_ossz_kg, r_atlag)