def fn1():
    print(f"Value: {value_1}")

def fn2(value_1):
    print(f"Value: {value_1}")

def fn3():
    value_1 = 20
    print(f"Value: {value_1}")

def fn4():
    value_2[1] = 999

def fn5():
    value_2[2] += 3

value_1 = 10
value_2 = [ 1, 2, 3]
print(f"Value is {value_2}")
fn2(value_2)
fn4()
fn2(value_2)
fn5()
fn2(value_2)
fn5()
fn2(value_2)