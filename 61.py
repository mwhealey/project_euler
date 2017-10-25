#do the math to figure out the ends of the ranges so the elements of these lists have the right length
l1 = [str(e*(e+1)/2) for e in range(45,141)] 
l2 = [str(e*e) for e in range(32,100)]
l3 = [str(e*(3*e-1)/2) for e in range(26,81)]
l4 = [str(e*(2*e-1)) for e in range(23,70)]
l5 = [str(e*(5*e-3)/2) for e in range(21,64)]
l6 = [str(e*(3*e-2)) for e in range(19,58)]

l = [l1,l2,l3,l4,l5,l6]

def all_perms(l): # recursively generations permuations of a list
    if len(l) <=1:
        yield l
    else:
        for perm in all_perms(l[1:]):
            for i in range(len(l)):
                yield perm[:i] + l[0:1] + perm[i:]

def match(s1,s2): # checks if the strings can chain together
    return s1[2:] == s2[:2]

def f(l): 
    '''
    recursively go through the elements of a list 
    that is within a list and find where where elements 
    of adjacent lists can be chained together 
    '''
    if len(l) == 2:
        a = []
        for e1 in l[0]:
            for e2 in l[1]:
                if match(e1,e2):
                    a.append((e1,e2))
        return a 
    a = []
    k = f(l[1:])
    if not k:
        return [] 
    for t in k:
        for e in l[0]:
            if match(e,t[0]):
                a.append((e,) + t)
    return a 

fl= 0 
for perm in all_perms(l):
    '''
    for every permutation of the list of lists produce the possible chainings
    that exist and check that the ends can chanin together
    '''
    fl = f(perm)
    for e in fl: # some permuations will have no possible chainings
        if match(e[5],e[0]):
            print sum(map(int,list(e)))
