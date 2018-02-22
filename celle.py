#Oppretter klassen Celle


class Celle:

#Setter alle celler til status doed i konstruktoeren
    def __init__(self):
        self._status = "Doed"

#Metode som setter status doed
    def settDoed(self):
        self._status = "Doed"

#Metode som setter status levende
    def settLevende(self):
        self._status = "Levende"

#Metode som sjekker om celle-objekt er levende eller doed
    def erLevende(self):
        if self._status == "Levende":
            return True
        else:
            return False

#Valgte aa definere string metoden slik at hentStatusTegn ble tolket som streng
    def __str__(self):
        return self.hentStatusTegn()

#Returnerer tilhoerende tegn for om cellen er levende eller doed
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else:
            return "."