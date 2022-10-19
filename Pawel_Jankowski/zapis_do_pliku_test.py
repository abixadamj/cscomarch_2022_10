from datetime import date
from datetime import datetime



plik = "Test2.txt"


with open(plik, "a") as file_to_save:
    for x in range(10):
        data = date.today()
        timeNow = datetime.now()
        file_to_save.write(f"{data} {timeNow} bleblelblelblelble.......\n")
