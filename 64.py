import math

def not_sqr(n):
    return int(math.sqrt(n))**2 != n

def process_inv_diff(s,m,f): 
    """
    returns the next set of an ints that define the fraction below the one defined by the paramaters
    for example: (23,4,1) represents (sqrt(23) - 4)/1 and outputs (1, 7, -3) which represents (1 + (sqrt(23)-3)/7
    so one can repeately generate down the cycle. 
    """
    p = int(f*(math.sqrt(s)+m)/(int(s)-int(m**2))) 
    d = (int(s)-int(m**2))/f
    return p,d,m-p*d

def get_cont_frac_len(n): # returns length of the cycle of continuous fractions
    l = []
    q = set([])
    p = int(math.sqrt(n))
    p,d,s = process_inv_diff(n,p,1)
    for e in range(500):
        p,d,s = process_inv_diff(n,int(math.fabs(s)),d)
        if (p,d,s) in q: # no need to measure the length of anything, once you see the same fraction twice you know you the cycle begins again i.e. has finished
            return len(q)
        else:
            q.add((p,d,s)) 

cnt = 0
for i in xrange(2,10000):
    if not_sqr(i):
        if get_cont_frac_len(i) % 2 == 1:
            cnt += 1 
print cnt
print process_inv_diff(23,4,1)
