def pal(s): # classic palindrome checking w/ recursion
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return pal(s[1:-1])
    return False

def reverse(n):
    return int(str(n)[::-1])

def run_iter(n): # run through the iterations to see if it ever produces a palindrom
    count = 1 
    n = n + reverse(n)
    while not pal(str(n)) and count <= 51:
        count += 1
        n = n + reverse(n)
    return pal(str(n))

count = 0
for i in range(1,10000): # just brute forcing through them all
    if not run_iter(i):
        print i
        count += 1
print count
