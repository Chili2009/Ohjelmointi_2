class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus
class Urheiluvaline:
    def __init__(self, paino):
        self.paino = paino
class Polkupyora(Kulkuneuvo, Urheiluvaline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluvaline.__init__(self, paino)

        self.vaihteet = vaihteet

pp = Polkupyora(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)