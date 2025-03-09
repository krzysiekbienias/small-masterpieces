import math

import math
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == 'bronze' and other.sword_type == 'bronze':
            return Sword('iron')
        if self.sword_type == 'iron' and other.sword_type == 'iron':
            return Sword("steel")
        else:
            raise Exception("cannot craft")


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        den = no.real ** 2 + no.imaginary ** 2

        return Complex((self.real * no.real + no.imaginary * self.imaginary) / den,
                       (no.real * self.imaginary - no.imaginary * self.real) / den)

    def mod(self):
        im = 0
        re = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(re, im)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
