# Wojtek

class Nbp_table:
    """
    Klasa obsługująca API NBP - tabelę walut
    """
    description = "To jest widoczne między obiektami - pole klasy"

    def __init__(self, table: str, waluta: str):
        self.table: str = table
        self.waluta: str = waluta
        self.kurs: float = 0
        self.nbp_tablica: dict = None
        self.nbp_table_no: str = ""
        self.error_text: str = None
        self.request_code: int = 0

    def get_table(self):
        if self.nbp_tablica is not None:
            self.error_text = "Jakaś tablica już tu jest..."
            return False

        import requests
        table_api = f"http://api.nbp.pl/api/exchangerates/tables/{self.table}/"
        try:
            r_api = requests.get(table_api)
        except ConnectionError:
            self.error_text = "Problem z siecią"
            return False
        except Exception as e:
            self.error_text = f"Inny błąd - {e}"
            return False

        self.request_code = r_api.status_code
        if self.request_code == 200:
            self.nbp_tablica = r_api.json()[0]
            self.nbp_table_no = self.nbp_tablica["no"]
            self.nbp_tablica = self.nbp_tablica["rates"]
            for rate in self.nbp_tablica:
                if rate['code'] == self.waluta:
                    self.kurs = rate['mid']
                    return True


    def show_currency(self):
        if self.request_code != 200:
            return False
        print(f"Dla waluty {self.waluta} w tablicy {self.nbp_table_no} kurs dzisiejszy wynosi {self.kurs}")


    def history_currency(self, start_date: str) -> list:
        """
        Pobieramy historię waluty self.waluta
        :param start_date: "RRRR-MM-DD" lub datetime.date()
        :return:
        """
        from datetime import date
        end_date = date.today()
        history_api = f"http://api.nbp.pl/api/exchangerates/rates/{self.table}/{self.waluta}/{start_date}/{end_date}/"
        import requests
        try:
            r_api = requests.get(history_api)
        except ConnectionError:
            self.error_text = "Problem z siecią"
            return False
        except Exception as e:
            self.error_text = f"Inny błąd - {e}"
            return False

        self.request_code = r_api.status_code
        if self.request_code == 200:
            historia_waluty = []
            for rate in r_api.json()['rates']:
                historia_waluty.append(rate['mid'])
            return historia_waluty
        else:
            self.error_text = f"Request error code: {self.request_code}"
            return False


if __name__ == "__main__":
    test_chf = Nbp_table("A", "CHF")
    test_usd = Nbp_table("A", "USD")
    test_chf.get_table()
    test_usd.show_currency()
    test_chf.show_currency()
    print(Nbp_table.description)
    print(test_usd.description)
    print(test_chf.description)
    dane = test_chf.history_currency("2022-02-01")
    print(dane)
