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
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")


class Talo:
    def __init__(self, alin=1, ylin=10, hissien_lukumaara=3):
        self.alin = alin
        self.ylin = ylin
        self.hissi_lista = [Hissi(alin, ylin) for _ in range(hissien_lukumaara)]

    def aja_hissi(self, hissin_numero, kerros):
        print(f"Hissin numero on {hissin_numero}")
        self.hissi_lista[hissin_numero - 1].siirry_kerrokseen(kerros)

    def palohalytys(self):
        print("Palohälytys!")
        for i in range(len(self.hissi_lista)):
            self.aja_hissi(i + 1, self.alin)


# Tehtävä 1
#h = Hissi(1, 10)
#h.siirry_kerrokseen(5)
#h.siirry_kerrokseen(1)

# Tehtävä 2
#t = Talo()
#t.aja_hissi(1, 9)
#t.aja_hissi(2, 4)
#t.aja_hissi(3, 5)
#t.palohalytys()
