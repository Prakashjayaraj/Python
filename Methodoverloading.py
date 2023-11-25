class Overload:
    def overload(self, a, b=None, c=None):
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c


overload = Overload()
num1 = overload.overload(11)
num2 = overload.overload(11, 11)
num3 = overload.overload(11, 11, 11)
print(num1)