cnt = 1 
for i in xrange(1,1000000): # quick and dirty if you run this and the it hangs after outputing the last possible result
    for n in range(1,50):
        if len(str(i**n)) == n:
            print cnt, (i,n)
            cnt += 1 
