from math import hypot, atan, sin, cos, sqrt

class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)
       
    def __abs__(self):
        return sqrt(self.r**2 + self.i**2)

    def __repr__(self):
        rep = 'Zespolona(' + str(self.r) + ',' + str(self.i) + ')'
        return rep

    def __str__(self):
        if self.i >= 0: return '(' + str(self.r) + '+' + str(self.i) + 'i)'
        return '(' + str(self.r) + str(self.i) + 'i)'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Zespolona(self.r + other, self.i)
        return Zespolona(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Zespolona(self.r - other, self.i)
        return Zespolona(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Zespolona(self.r * other, self.i * other)
        return Zespolona((self.r * other.r) - (self.i * other.i), (self.i * other.r) + (self.r * other.i))

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = Zespolona(other, 0)
        return self.__sub__(other)

    def __eq__(self, other):
        return self.r == other.r and self.i == other.i

    def __ne__(self, other):
        return self.r != other.r or self.i != other.i

    def __pow__(self, other):
        my_abs = abs(self)
        my_arg = self.argz() * other
        my_sin = sin(my_arg)
        my_cos = cos(my_arg)
        my_pow = my_abs ** other
        return Zespolona(int(my_pow * my_cos), int(my_pow * my_sin))


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a ==  b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)