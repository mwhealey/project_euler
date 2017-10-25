import math

def sym(s1,s2):
    return is_prime(str(s1)+str(s2)) and is_prime(str(s2)+str(s1))

def symt(e,ts):
    for t in ts:
        if not sym(e,t) or e == t:
            return False 
    return True

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

p = list(primes_sieve(10**7))

def is_prime(n):
    if isinstance(n,str):
        n = int(n)
    if n == 1:
        return False
    sq = math.sqrt(n)
    for e in p:
        if e >= sq:
            return 1
        if n % e == 0: 
            return 0 
    return 1


def disj(t1,t2):
    for e in t1:
        if e in t2:
            return False
    return True

def f(l):
    #recursively generate sets of primes that have the desired condition measured by sym and symt
    if len(l)==2:
        for i in l[0]:
            l[1].remove(i) # this prevents passing up tuples where the only difference is order
            for e in l[1]:
                if sym(i,e):
                    yield (i,e)
    else:
        for t in f(l[1:]): 
            for e in l[0]:
                if symt(e,t):
                    yield (e,)+(t)

primes = list(primes_sieve(10**4))
l = [list(primes_sieve(10**4))]*4
s = set([])
for e in f(l): # get sets of four primes that work and we know one is a subset of the target set w/ cardinality 5
    s.add(e)

for t in s:
    for e in primes:
        if symt(e,t):
            print e,t

