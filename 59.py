import math 
import string 

def decrypt(s,k):
    s_d = ''
    k_long = int(math.ceil(len(s) / 3.0))*k 
    for i in range(len(s)):
        s_d += chr(s[i] ^ ord(k_long[i]))
    return s_d

summ = 0
with open('p059_cipher.txt') as f:
    s = map( int , f.readlines()[0].split(','))
    keys = []
    times = math.ceil(len(s) / 3.0) 
    for c1 in string.lowercase:
        for c2 in string.lowercase:
            for c3 in string.lowercase:
                k = c1 + c2+ c3
                keys.append(k)
    for k in keys:
        d = decrypt(s,k)
        if ' the ' in d and ' is ' in d and ' of ' in d: 

            '''
            as per their recommendation i am seeking common words however
            a more sophisticated technique is to match up character counts to natural english 
            '''

            for e in d:
                summ += ord(e)
            print d, summ
