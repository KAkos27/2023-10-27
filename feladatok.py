#Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
def elso():
    i: int = 0
    b: int = 0
    while i != 10:
        a: int = int(input("Kérek egy számot: "))
        i+=1
        if a % 3 == 0:
            b+=1
    print(f"Ennyi 3-mal osztható számot adtál meg: {b}")

#Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
def masodik(): 
    a: int = int(input("Kérek egy számot: "))
    while a % 10 != 0:
        print("10-zel osztható számto kell magadni")
        a: int = int(input("Kérek egy számot: "))
    print(f"A(z) {a} egy 10-zel osztható szám")

#Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def harmadik():
    a: int = int(input("Kérek egy számot: "))
    while not (100 > a >= 10 and (a % 2 == 0)):
        print("Kétjegyű páros számot kell megadni!")
        a: int = int(input("Kérek egy számot: "))
    print(f"A(z) {a} egy kétjegyű páros szám")

#Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*
def negyedik():
    a: int = int(input("Kérek egy számot: "))
    while not (a > 0 and (a % 2 != 0)):
        print("Pozitív páratlan számot kell megadni!")
        a: int = int(input("Kérek egy számot: "))
    print(f"A(z) {a} egy poztiív páratlan szám")

#Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.
def otodik():
    a: int = int(input("Kérek egy számot: "))
    gyok: float = a ** 0.5 
    while not (gyok.is_integer() or (a % 3 == 0)):
        print("Gyökszámot vagy 3-mal osztható számot kell megadni!")
        a: int = int(input("Kérek egy számot: "))
        gyok: float = a ** 0.5 
    print(f"A(z) {a} egy gyökszám vagy 3-mal osztható")

#Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!
def hatodik():
    a: int = int(input("Kérek egy számot: "))
    b: int = int(input("Kérek egy számot: "))
    c: int = int(input("Kérek egy számot: "))

    while not ((a < b + c) and (b < a + c) and (c < a + b)):
        print("Az oldalak amiket megadtál nem felelnek meg a háromszög-oldalegynlőtlenségnek")
        a: int = int(input("Kérek egy számot: "))
        b: int = int(input("Kérek egy számot: "))
        c: int = int(input("Kérek egy számot: "))
    print(f"A(z) {a} meg a(z) {b} meg a(z) {c} egy szerkeszthető háromszöget alkot.")

#Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
def hetedik():
    a: str = str(input("Adj meg egy tetszőleges szöveget: "))
    while (len(a) < 3):
        print("Minimum 3 karakter legyen!")
        a: str = str(input("Adj meg egy tetszőleges szöveget: "))
    print(a.upper())

#Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
def nyolcadik():
    a: str = str(input("Adj meg egy tetszőleges szöveget: "))
    hossz = len(a)
    while not(a.islower() and (hossz == 4)):
        print("Rossz szöveget adtál meg")
        a: str = str(input("Adj meg egy tetszőleges szöveget: "))
        hossz = len(a)
    print("Jó szöveget adtál meg")

#Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!
def kilencedik():
    a: int = int(input("Kérek egy számot: "))
    while a < 0:
        a: int = int(input("Kérek egy POZITÍV számot: "))
    i: int = 0
    osszeg: int = 0
    osszeg += a
    
    while a != 0: 
        a: int = int(input("Kérek egy számot: "))
        while a < 0:
            a: int = int(input("Kérek egy POZITÍV számot: "))
        i += 1
        osszeg += a
    szamolas = (osszeg / i)
    print(round(szamolas, 2))