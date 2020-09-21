class FieldElement:
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = "num {} is not in field range 0 to {}".format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime and other.prime

    def __ne__(self, other):
        return not(self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't add two number differ fields")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't add two number differ fields")
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Can't add two number differ fields")
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)


field1 = FieldElement(2, 3)
field2 = FieldElement(2, 3)
field3 = FieldElement(3, 7)
field4 = FieldElement(3, 13)
field5 = FieldElement(12, 13)
field6 = FieldElement(10, 13)

field7 = FieldElement(3, 31)
field8 = FieldElement(24, 31)

print(field1 == field2)
print(field1 != field3)
print(field1 + field2)
print(field1 - field2)
print(field4*field5)
print(field1**3)
print(field5 / field6)
print(field7 / field8)

