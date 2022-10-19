def hi_hello(name: str, age: int):
    if type(name) is not str:
        return None

    ret_value = f"Cześć {name} - masz {age} lat;-)"

    if age >= 18:
        ret_value += " - hej - jesteś dorosły(a)"
        return ret_value
    else:
        ret_value += f"brakuje ci {18 - age} lat."
        return ret_value



print("Cześć")
my_age = 44
my_name = 33 # "Adam"
print(my_age)
hi_hello(my_name, my_age)
value = hi_hello(my_name, my_age)
print(value)
