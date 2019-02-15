# --------------
import pandas as pd
import numpy as np
import math
import cmath


#Code starts here
class complex_numbers:

    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))

    def __add__(self,other):
        """Overloaded '+' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.
        """
        x = self.real + other.real
        y = self.imag + other.imag
        return complex_numbers(x,y)
    
    def __sub__(self,other):
        """Overloaded '-' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.
        """
        x = self.real - other.real
        y = self.imag - other.imag
        return complex_numbers(x,y)

    def __mul__(self,other):
        """Overloaded '*' operator.

        Args:
        param1 (complex_numbers): Other point.

        Returns:
        complex_numbers: The evaluated complex number.
        """
        x = self.real * other.real
        y = self.imag * other.imag
        w=x-y
        z=x+y
        return complex_numbers(w,z)

    def __truediv__(self,other):
        # r1=self.real
        # i1-self.imag
        # r2=other.real
        # i2=other.imag
        resultR=float(float(self.real*other.real+self.imag*other.imag)/float(other.real*other.real+other.imag*other.imag))
        resultI=float(float(other.real*self.imag-self.real*other.imag)/float(other.real*other.real+other.imag*other.imag))
        
        return complex_numbers(resultR,resultI)

    def absolute(self):
        self.x = math.sqrt((self.real**2)+(self.imag**2))
        return self.x

    def argument(self):
        y=np.arctan([self.imag/self.real])
        return math.degrees(y)
    
    def conjugate(self):
        a=np.conj(self.real)
        b=np.conj(self.imag)
        return complex_numbers(a,-b)

comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)

comp_sum=comp_1.__add__(comp_2)

comp_diff=comp_1.__sub__(comp_2)

comp_prod=comp_1.__mul__(comp_2)

comp_quot=comp_1.__truediv__(comp_2)

comp_abs=comp_1.absolute()

comp_conj=comp_1.conjugate()

comp_arg=comp_1.argument()


