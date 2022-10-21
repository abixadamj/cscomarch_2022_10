#Marek Skowronek


# Marek
# talkPython.fm podcasty o python, po angielsku, w miarę tanie, kody na git.
# przeciążenie to metoda super()
#


class Maker:  # nazwa klasy musi być różna od nazwy modułu
    def __init__(self, surname: str):  # chyba jak kontruktory w C#, a self to nazwa konkretnego obiektu, :str to zabezpiecza przed blędnym typem
        self.maker_name = "DUMMY"
        self.maker_surname = surname

    def show_name(self):
        print(f"Imię: {self.maker_name} nazwisko: {self.maker_surname}")

janusz = Maker(surname="Skowornek")

print(janusz.maker_surname)

janusz.show_name()
