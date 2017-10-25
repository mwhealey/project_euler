import math
from decimal import Decimal

def add_frac(a,(n,d)): # a+(n/d) = (d*a+n)/d
    return (d*a+n,d) 

l = [2]
for e in xrange(1,34): # generate the sequence
    l+= [1,2*e,1]

t = add_frac(l[-2],(1,l[-1])) # start up the cycle at the end of the sequence 

for e in l[:-2][::-1]: # procede through the sequence in reverse to build up numerator and denomator, swap tuple elements since fractions get inverted
    t = add_frac(e,(t[1],t[0]))
print reduce(lambda x,y: int(x)+int(y), str(t[0])) #add up numbers in numerator
