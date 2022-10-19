from podstawowy_import import *
from datetime import date
import requests
import json

plik = uniq_file()
data = date.today()
table = "A"
table_api = f"http://api.nbp.pl/api/exchangerates/tables/{table}/"
waluty = ("USD", "EUR", "CHF", "GBP")

r_api = requests.get(table_api)

# print(r_api.text)
table_as_list = r_api.json()
table_as_dict = table_as_list[0]
table_number = table_as_dict["no"]
table_rates = table_as_dict["rates"]
table_as_json = json.dumps(table_as_list, indent=2)

print(table_rates)

with open(plik, "w") as file_to_save:
    file_to_save.write(f"Tablica kursów walut z dnia {data}\n")
    file_to_save.write(f"Tablica nr: {table_number}\n")
    file_to_save.write("=========================================\n")
    file_to_save.write("Currency         | Code | Mid \n")
    for any_currency in table_rates:
        text = any_currency['currency'].ljust(30) + "| "
        text += any_currency['code'] + "| "
        text += str(any_currency['mid']) + "\n"
        if any_currency['code'] in waluty:
            file_to_save.write(text)
    file_to_save.write("=========================================\n")
