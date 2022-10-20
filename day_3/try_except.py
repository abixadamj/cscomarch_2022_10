try:
    print("Siemka")
except:
    print("Nie udało się")

# przykład błędu

try:
    # wynik = 3 / 0
    # wynik = "A" / 10
    # print(wynik)
    pass
except ZeroDivisionError:
    print("Nie dziel przez 0")
except NameError:
    print("Brak zmiennej!!!")
except TypeError:
    print("Bład typu!!!!")
except Exception as e:
    print(f"Błąd!!!! - {e}")