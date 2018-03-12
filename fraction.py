# class that model a Fraction


"""
Notice that the formal parameter list contains three items (self, top, bottom). 
self is a special parameter that will always be used as a reference back to the object itself.
 It must always be the first formal parameter; however, it will never be given 
 an actual parameter value upon invocation. As described earlier, fractions require two pieces of 
 state data, the numerator and the denominator

 The notation self.num in the constructor defines the fraction object to have an internal
  data object called num as part of its state. Likewise, self.den creates the denominator. 
  The values of the two formal parameters are initially assigned to the state, allowing the 
  new fraction object to know its starting value.
"""
#we use python special methods __add__ and __str__

def gcd(m,n):
        while m%n !=0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn

        return n

print(gcd(20,10))

class Fraction:

    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

    def __str__(self):
        return str(self.num) + '/' + str(self.deno)

    

   

        #in order to add two fractions , denominators should be the same or multiply them

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.deno + self.deno*otherfraction.num
        newdeno = self.deno*otherfraction.deno
        common = gcd(newnum, newdeno)
        
        return Fraction(newnum//common, newdeno//common)

    

myfraction = Fraction(3,5)

print(myfraction)

print("Zosi eat "+ str(myfraction) +" of ugali each day.")

# adding two fractions

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print(f3)

#print(f1.__add__f2())
