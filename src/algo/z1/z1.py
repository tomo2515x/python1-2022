def add(a, b):
    print(a + b)


def mul(a, b):
    print(a * b)

def calculate(fn, a, b):
    if fn == "add": return add(a,b)
    return mul(a,b)

print(calculate("add", 1, 2))
print(calculate("mul", 1, 2))
