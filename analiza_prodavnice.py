import random
import math

#1 Kreirati listu proizvoda Lista treba da sadrži najmanje 8 naziva proizvoda (string).
proizvodi = [
    "Televizor", "Tablet", "Bluetooth zvučnik", 
    "Web kamera", "Mehanička tastatura", "Gejmerski miš", 
    "SSD disk", "Slušalice sa mikrofonom"
]

#2 Kreirati rečnik koji svakom proizvodu dodeljuje cenu u evrima (float). Primer: { "Laptop": 950.99, "Miš": 19.99, ... }
cene = {
    "Televizor": 450.00,
    "Tablet": 220.50,
    "Bluetooth zvučnik": 45.99,
    "Web kamera": 89.00,
    "Mehanička tastatura": 110.00,
    "Gejmerski miš": 55.45,
    "SSD disk": 75.20,
    "Slušalice sa mikrofonom": 35.00
}

#3 Prikazati korisniku na standardnom izlazu sve proizvode i njihove cene u formatu:
print("--- Ponuda proizvoda ---")
for artikal in proizvodi:
    iznos = cene[artikal]
    print(f"{artikal} - {iznos:.2f} €")
print("-" * 30)

#4 Od korisnika tražiti unos budžeta (float). Ispisati koje proizvode korisnik može da priušti, koristeći petlju i uslov.
try:
    budzet = float(input("Unesite vaš budžet u evrima: "))
    print(f"\nSa budžetom od {budzet} € možete kupiti:")
    
    mogu_kupiti = []
    for artikal in proizvodi:
        if cene[artikal] <= budzet:
            mogu_kupiti.append(artikal)
            print(f"- {artikal} ({cene[artikal]} €)")
            
    if not mogu_kupiti:
        print("Nažalost, nemate dovoljno novca ni za jedan proizvod.")
except ValueError:
    print("Greška: Molimo unesite brojčanu vrednost za budžet.")

print("-" * 30)

#5 Funkcija najskuplji_proizvod() Funkcija treba da vrati najskuplji proizvod iz rečnika. Pozvati je i prikazati rezultat.
def najskuplji_proizvod(podaci_o_cenama):
    # Inicijalizacija sa prvim ključem iz rečnika
    max_artikal = list(podaci_o_cenama.keys())[0]
    for artikal in podaci_o_cenama:
        if podaci_o_cenama[artikal] > podaci_o_cenama[max_artikal]:
            max_artikal = artikal
    return max_artikal

skuplji = najskuplji_proizvod(cene)
print(f"Najskuplji proizvod u prodavnici je: {skuplji} ({cene[skuplji]} €)")

#6 Korišćenje random modula simulirati da je korisnik kliknuo na nasumičan proizvod iz liste. Ispisati poruku: Korisniku je privukao pažnju proizvod: __
kliknuti_proizvod = random.choice(proizvodi)
print(f"Korisniku je privukao pažnju proizvod: {kliknuti_proizvod}")

#7 Korišćenje math modula Izračunati i zaokružiti prosečnu cenu svih proizvoda na dve decimale.
ukupna_suma = sum(cene.values())
broj_artikala = len(cene)
prosek = ukupna_suma / broj_artikala
# Zaokruživanje na dve decimale koristeći f-string ili round()
print(f"Prosečna cena svih proizvoda je: {math.fsum(cene.values()) / len(cene):.2f} €")

#8 Uvesti broj prodatih komada svakog proizvoda (druga lista sa istom dužinom). Na osnovu toga izračunati ukupan prihod (sumom cena × količina).
prodati_komadi = [3, 10, 15, 5, 12, 25, 18, 40]
ukupni_prihod = 0

print("\n--- Analiza prodaje i prihoda ---")
for i in range(len(proizvodi)):
    naziv = proizvodi[i]
    kolicina = prodati_komadi[i]
    cena_po_komadu = cene[naziv]
    prihod_po_artiklu = kolicina * cena_po_komadu
    ukupni_prihod += prihod_po_artiklu
    print(f"{naziv:25} | Prodato: {kolicina:2} | Prihod: {prihod_po_artiklu:>8.2f} €")

print(f"UKUPAN PRIHOD PRODAVNICE: {ukupni_prihod:.2f} €")
print("-" * 30)

#9 Dodati još jedan novi proizvod u sistem ― ažurirati listu i rečnik. Ispisati ažuriranu listu proizvoda.
novi_artikal = "Eksterni monitor"
nova_cena = 155.00
proizvodi.append(novi_artikal)
cene[novi_artikal] = nova_cena

print("Ažurirana lista svih proizvoda nakon proširenja asortimana:")
print(proizvodi)
print("-" * 30)

#10 Ispis proizvoda sortirano po ceni. Sortirati proizvode od najjeftinijeg ka najskupljem i ispisati ih u istom formatu kao u zadatku 3:
sortirani = sorted(cene.items(), key=lambda stavka: stavka[1])

print("Proizvodi sortirani po ceni (rastuće):")
for naziv, cena_artikla in sortirani:
    print(f"{naziv} - {cena_artikla:.2f} €")
