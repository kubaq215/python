from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x):
        super().__init__(x, x)

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(prostokat):
    print("Pole: Prostokat")
    return prostokat.x * prostokat.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x, y):
    a = Prostokat(x, y)
    return pole(a)

@dispatch(Kwadrat)
def pole(kwadrat):
    print("Pole: Kwadrat")
    return kwadrat.x * kwadrat.y

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x):
    a = Kwadrat(x)
    return pole(a)

# testy

a, b, c = Figura(), Prostokat(2,4), Kwadrat(2)

bb = pole(b, 5, 6)
print(bb)
cc = pole(c, 7)
print(cc)


def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i)) # polymorphism at runtime

polaPowierzchni([a,b,c])