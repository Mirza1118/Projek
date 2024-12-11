class Hewan:
    def __init__(self, species, makanan):
        self.species = species
        self.makanan = makanan
    def bunyi_hewan(self):
        print(f"{self.species} suka makan {self.makanan}")
hewan_1 = Hewan("kucing", "whiskas")
hewan_1.bunyi_hewan()
hewan_2 = Hewan("ayam", "biji-bijian")
hewan_2.bunyi_hewan()       