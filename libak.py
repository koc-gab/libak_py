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

def eldontes1(l):
    van=False
    i=0
    while i<len(l) and not l[i]>=3:
        i+=1
    if i<len(l):
        van=True
    return van

def eldontes2(l):
    i=len(l-1)
    while i>0 and not (l[i]>l[i-1]):
        i-=1
    if i<len(l):
        van=True
    else:
        van=False
    return van
    
def kiir(l, rmog, ra, rlhs, rlklens):
    print(f"A libák súlyai: {l}")
    print(f"{rmog}kg libát ehet meg a róka.")
    print(f"Átlagosan {ra}kg-os libákat eszik a róka.")
    print(f"{rlhs}, hogy a róka 3kg-os libát lopott.")
    print(f"{rlklens}, hogy a róka kisebb libát hozott, mint az előző napon.")

# FőPROGRAM #
#Input
libak=beker()
#Számítás
r_megehet_ossz_kg=osszegzes(libak)
r_megehet_db=megszamolas(libak)
r_atlag=r_megehet_db/r_megehet_db
r_legalabb_3=eldontes1(libak)
if r_legalabb_3:
    r_legalabb_3_str="Előfordult"
else:
    r_legalabb_3_str="Nem fordult elő"
r_lopott_kisebb_libat_elozo_nap=eldontes2(libak)
if r_lopott_kisebb_libat_elozo_nap:
    r_lopott_kisebb_libat_elozo_nap_string="Előfordult"
else:
    r_lopott_kisebb_libat_elozo_nap_string="Nem fordult elő"
#Output
kiir(libak, r_megehet_ossz_kg, r_atlag, r_legalabb_3_str, r_lopott_kisebb_libat_elozo_nap_string)