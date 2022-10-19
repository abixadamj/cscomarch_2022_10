# Adam

class Referencyjna:
    def __init__(self, nowy_kolor: str):
        self.nazwa = "Jakaś tam nazwa"
        self.kolor = nowy_kolor

    def jaki_kolor(self):
        print(f"Narzędzie ma kolor {self.kolor} i nazywa się {self.nazwa}")

srb_czerw = Referencyjna("czerwony")
print(srb_czerw.kolor)
srb_czerw.jaki_kolor()