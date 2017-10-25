def get_bucket(n): # a set of permutations of a string maps uniquely to a histogram of of the characters in the string 
    l = [0]*10
    for e in n:
        l[int(e)] += 1
    return tuple(l) 

d = {}

for i in xrange(20000):
    e = str(i**3)
    k = d.get(get_bucket(e),False)
    if k:
        k.append(e) 
    else:
        d[get_bucket(e)] = [e] 

for k,v in d.items():
    if len(v) == 5 :
        print sorted(v)

