class Fraction:
    numerator = 1
    denominatior = 1

    def init(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def init():
        pass

    def simplify(self):
        num = 2
        while True:
            if numerator % num == 0 and denominator % num == 0:
                numerator = numerator/num
                denominator = denominator/num
            elif(not(num > numerator or num > denominator)):
                num += 1
            else:
                break
        del(num)

    def __add__(self, f):
        rf, nf1, nf2 = Fraction()
        a = Fraction(self.denominator, self.denominator)
        b = Fraction(f.denominator, f.denominator)
        nf1.numerator = self.numerator * b.numerator
        nf1.denominator = self.denominator * b.denominator
        nf2.numerator = f.numerator * a.numerator
        nf2.denominator = f.denominator * a.denominator
        rf.numerator = nf1.numerator + nf2.numerator
        rf.denominator = nf1.denominator
        rf.simplify()
        del(nf1, nf2, a, b)
        return rf

    def __sub__(self, f):
        rf, nf1, nf2 = Fraction()
        a = Fraction(self.denominator, self.denominator)
        b = Fraction(f.denominator, f.denominator)
        nf1.numerator = self.numerator * b.numerator
        nf1.denominator = self.denominator * b.denominator
        nf2.numerator = f.numerator * a.numerator
        nf2.denominator = f.denominator * a.denominator
        rf.numerator = nf1.numerator - nf2.numerator
        rf.denominator = nf1.denominator
        del(nf1, nf2, a, b)
        rf.simplify()
        return rf

    def __mul__(self, f):
        newf = Fraction()
        newf.numerator = self.numerator * f.numerator
        newf.denominator = self.denominator * f.denominator;            
        newf.simplify();            
        return newf
    
    def __truediv__(self, f):
        newf = Fraction()
        newf.numerator = self.numerator * f.denominator
        newf.denominator = self.denominator * f.numerator 
        newf.simplify()
        return newf

    def __str__(self):
        if self.denominator == 1:
            return self.numerator
        
        elif self.denominator == 0:
            return 0
        else:
            return f"{self.numerator}/{self.denominator}"

    def toDouble(self):
        return self.numerator/self.denominator
    
    def __mod__(self, f):
        newf = Fraction()
        newf.numerator = self.numerator * f.denominator
        newf.denominator = self.denominator * f.numerator
        whole = newf.numerator/newf.denominator
        remainderN = whole * newf.denominator
        remainder = Fraction(remainderN, newf.denominator)
        remainder = newf - remainder
        remainder.simplify()
        del(newf, whole, remainderN)
        return remainder

class SlopeIntForm:
    def init(self, y, m, x, b):
        self.y = y
        self.m = m
        self.x = x
        self.b = b

    def init(self, m, b):
        self.m = m
        self.b = b

    def slopeIntFromPoints(a, b):
        slope = Fraction()
        slope.numerator((b.x - a.x).toDouble())
        slope.denominatior((b.y - a.y).toDouble())
        be = Fraction()
        equation = SlopeIntForm(slope, be)
        return equation