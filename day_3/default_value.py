def fun1(value: str, def_value: int = 10):
    print(value * def_value)

def fn2(value: str, def_value: int = 10, def_sep: str = "*"):
    print((value+def_sep) * def_value)

fun1("A*")
fun1("B*", 4)

fn2("C")
fn2("D", def_sep="^")