"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
versenyzok = []
with open('beolvasando_adatok/f1.txt', 'r') as f:
    next(f)
    for sor in f:
        adatok = sor.strip().split(';')
        adat = {'Név:': adatok[0], "Csapat:": adatok[1], "Győzelmek: ": adatok[2], "Futamok:": adatok[3]}
        versenyzok.append(adat)

osszes = len(versenyzok)

legtobb_gyoztes = 0
legtobb_gyoztes_nev = ""
legtobb_futam = 0

for versenyzo in versenyzok:
    if int(versenyzo["Győzelmek: "]) > legtobb_gyoztes:
        legtobb_gyoztes = int(versenyzo["Győzelmek: "])
        legtobb_gyoztes_nev = versenyzo["Név:"]

    if int(versenyzo["Futamok:"]) > legtobb_futam:
        legtobb_futam = int(versenyzo["Futamok:"])
        legtobb_futam_nev = versenyzo["Név:"]

# print(versenyzok)

atlag = 0
osszes_futam = 0
for versenyzo in versenyzok:
    osszes_futam += int(versenyzo["Futamok:"])
    atlag += int(versenyzo["Futamok:"])

atlag = atlag / osszes


w_osszes = f"A beolvasott fájlban összesen {osszes} versenyző szerepel."
w_gyoztes = f"A legtöbb futamot nyert versenyző: {legtobb_gyoztes_nev}"
w_legtobb = f"A legtöbb futamot teljesített versenyző: {legtobb_futam_nev}"
w_atlag = f"Az átlagos futamszám: {atlag:.0f}"

print(f" {w_osszes},\n {w_gyoztes},\n {w_legtobb},\n {w_atlag}")

with open('kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as kiirando:
    kiirando.write(str(w_osszes))
    kiirando.write(str("\n"+ w_gyoztes))
    kiirando.write(str("\n"+ w_legtobb))
    kiirando.write(str("\n"+ w_atlag))
    print("× statisztika.txt fájl sikeresen kiírva ×")