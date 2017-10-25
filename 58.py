# This was one of the best PE problems i have seen.

from __future__ import division
import math 

def primes_sieve(limit):
    # sieve of eranthoses with some optimization
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

p = list(primes_sieve(10000000))

def is_prime(n):
    sq = math.sqrt(n)
    for e in p:
        if e >= sq:
            return 1
        if n % e == 0: 
            return 0 
    return 1

total_primes = 0 
total = 1  # this is for the center of the spiral

for e in xrange(1,800000): # just use some arbitrarily high number
    r1,r2,r3 = (4*e*e+2*e+1),(4*e*e+1),(4*e*e-2*e+1)
    """ 
    These formulas are for three corners of the growing spiral they
    come from light analysis of the patterns (confirm them for yourself), 
    the lower right is always a square and so never prime and not worth computing.
    """
    total_primes += sum([is_prime(r1), is_prime(r2), is_prime(r3)]) # add up the primes 
    total += 4 
    if total_primes/total <.1:
        print 2*e+1 # the length of the side
        break
    
