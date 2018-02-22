#Importerer metoder og funksjoner fra andre klasser
from celle import *
from spillebrett import *


#Definerer hovedprogrammet hvor objektene opprettes og meny-loekken som vises
#i terminal. Lager og en while loekke slik at bruker kan se saa mange
#generasjoner han/hun vil av brettet.
def hovedprogram():
    rader = int(input("Skriv inn antall rader: "))
    kolonner = int(input("Skriv inn antall kolonner: "))
    brett1 = Spillebrett(rader, kolonner)
    print("\nGenerasjon: 0")
    print("Antall levende celler: ", brett1.finnAntallLevende())
    brett1.tegnBrett()
    while True:
        valg = input("\nTrykk enter for aa gaa videre \neller 'q' for aa avslutte:\n")
        if valg == "":
            print("Generasjon:", brett1.oppdatering())
            print("Antall levende celler: ", brett1.finnAntallLevende())
            brett1.tegnBrett()
        elif valg.lower() == "q":
            break

#Kaller paa hovedprogram metoden
hovedprogram()