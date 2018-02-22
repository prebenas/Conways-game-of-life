from random import randint
from celle import *


#Oppretter klassen Spillebrett


class Spillebrett:

#Oppretter variablene som skal brukes i metodene senere
#Samt oppretter rutenett med celle-objekter
    def __init__(self, rader, kolonner):
        self.generasjonsnummer = 0
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        for i in range(self._rader):
            self._rutenett.append([])
            for j in range(self._kolonner):
                self._rutenett[i].append(Celle())
        self.generer()

#Oppretter metoden tegnBrett som ved hjelp av map (nestet for loekke, med append funksjon)
#og formatering printer listen av lister i rutenett form
    def tegnBrett(self):
        for i in self._rutenett:
            print(" ".join(map(str, i)))
        print()

#Oppdatering! Opprettet teller inni for-loekken, fant naboer ved hjelp av finnNabo,
#og sjekket om de var levende, om de var det, inkrementerte teller.
#Av de testene jeg har kjoert ser det ut til aa fungere naa
    def oppdatering(self):
        self.generasjonsnummer += 1
        doedeSkalLeve = []
        levendeSkalDoe = []
        for r, rad in enumerate(self._rutenett):
            for c, celle in enumerate(rad):
                teller = 0
                for nabo in self.finnNabo(r, c):
                    if nabo.erLevende():
                        teller += 1
                if celle.erLevende() is True:
                    if teller < 2 or teller > 3:
                        levendeSkalDoe.append(celle)
                    elif teller == 2 or teller == 3:
                        doedeSkalLeve.append(celle)
                elif celle.erLevende() is False:
                    if teller == 3:
                        doedeSkalLeve.append(celle)
        for i in levendeSkalDoe:
                i.settDoed()
        for i in doedeSkalLeve:
                i.settLevende()
        return self.generasjonsnummer

#Metode som generer tilfeldige celler i brettet
    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0, 3)
                if rand == 3:
                    self._rutenett[i][j].settLevende()

#Metode som finner alle naboene til en celle og lagrer dem i en liste
    def finnNabo(self, rad, kolonne):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboRad = rad + i
                naboKolonne = kolonne + j
                if(naboRad == rad and naboKolonne == kolonne) is not True:
                    if(naboRad < 0 or naboKolonne < 0 or naboRad >
                    self._rader - 1 or naboKolonne > self._kolonner - 1) is not True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste

#Metode som finner hvor mange celler som er levende og returnerer tallet
    def finnAntallLevende(self):
        self._levende = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende() is True:
                    self._levende += 1
        return self._levende