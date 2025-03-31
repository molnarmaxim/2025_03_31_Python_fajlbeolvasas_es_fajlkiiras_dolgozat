"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

with open('beolvasando_adatok/f1.txt', 'r') as f:
    next(f)
    versenyzok = [sor.strip().split(';') for sor in f]
    osszes = len(versenyzok)
    gyoztes_futamok = versenyzok[2]

print(versenyzok)
print(gyoztes_futamok)



print(f"A beolvasott fájlban összesen {osszes} versenyző szerepel.")
print("A legtöbb futamot nyert versenyző: ____")
print("A legtöbb futamot teljesített versenyző: ____")
print("Az átlagos futamszám: ____")