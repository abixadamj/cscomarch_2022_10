class Jakas:
    def __init__(self, kolor: str):
        self.kolor = kolor

    def __str__(self):
        return f"To jest coś o kolorze {self.kolor}"

test = Jakas("czerwony")

print(test)

# from datetime import date
# date.today()
# datetime.date(2022, 10, 21)
# dir(date.today())
# ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'ctime', 'day', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 'today', 'toordinal', 'weekday', 'year']
# date.today().isoformat()
# '2022-10-21'
# date.today().weekday()
# 4
# f"Data: {date.today}"
# 'Data: <built-in method today of type object at 0x55c12d4d96c0>'
# f"Data: {date.today()}"
# 'Data: 2022-10-21'
