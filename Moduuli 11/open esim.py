class Tyontekija:
    tyontekijoiden_lkm = 0

    def __init__(self, etunimi, sukunimi):
        Tyontekija.tyontekijoiden_lkm = Tyontekija.tyontekijoiden_lkm + 1
        self.tyontekija_nro = Tyontekija.tyontekijoiden_lkm #luodaan uusi ominaisuus nro uusi muuttuja
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def  tulosta_tiedot(self):
        print(f"{self.tyontekija_nro}: {self.etunimi} {self.sukunimi}")
class Tuntipalkkainen(Tyontekija):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):#tulostaa rivi 10 ja antaa 11 rivin
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Tyontekija):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.kokopalkka = kokopalkka
        super().__init__(etunimi, sukunimi)
    def tulosta_tiedot(self):  # tulostaa rivi 10 ja antaa 11 rivin
        super().tulosta_tiedot()
        print(f"kokopalkka: {self.kokopalkka}")


#Anthony.tulosta_tiedot()

#Anthony = Tuntipalkkainen("Anthony", "Valtanen", 10)

tyontekijat = []
tyontekijat.append(Tuntipalkkainen("Anthony", "Valtanen", 10))
tyontekijat.append(Kuukausipalkkainen("Mia", "Fernandez", 50))

for t in tyontekijat:
    t.tulosta_tiedot()



