import random
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
    def siirry_kerrokseen(self, kerros):
        while self.kerros < kerros and self.kerros < self.ylin:
            self.kerros_ylos()
        while self.kerros > kerros and self.kerros > self.alin:
            self.kerros_alas()
    def kerros_ylos(self):
        self.kerros += 1
        print(f"hissi on kerroksessa {self.kerros}")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"hissi on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin=1, ylin=10, hissi_lista=None, hissien_Lukumäärä=3):
        self.alin = alin
        self.ylin = ylin
        if hissi_lista is None:
            hissi_lista = []
        self.hissi_lista = hissi_lista
        self.hissien_Lukumäärä = hissien_Lukumäärä
        if hissien_Lukumäärä:
            for i in range(0, 10):
                hissi_lista.append(Hissi(alin, ylin))
    def aja_hissiä(self, hissin_Numero, kerros):
            print(f"hissi numero {hissin_Numero} on:")
            self.hissi_lista[hissin_Numero].siirry_kerrokseen(kerros)
    def palohälytys(self):
        print(f"Palohälytys!")
        for i in range(0, self.hissien_Lukumäärä):
            self.aja_hissiä(1 + i, self.alin)

#teht 1
h = Hissi(1,10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

#teht 2
t = Talo()
t.aja_hissiä(1,9)
t.aja_hissiä(2,4)
t.aja_hissiä(3,5)
t.palohälytys()
