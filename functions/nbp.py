# Wojtek

class Nbp_table:
    def __init__(self, nowy_kolor):
        self.nazwa = "Jakaś tam nazwa"
        self.kolor = nowy_kolor

    def jaki_kolor(self):
        print(f"Narzędzie ma kolor {self.kolor} i nazywa się {self.nazwa}")

srb_czerw = Nbp_table("czerwony")
srb_czerw.jaki_kolor()