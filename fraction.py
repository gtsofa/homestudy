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

class Fraction:

    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

myfraction = Fraction(3,5)

print(myfraction)
