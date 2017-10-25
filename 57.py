prev_j,j = 1, 3 
prev_k,k = 1, 2
count = 0
for i in range(1000):
    if len(str(k)) != len(str(j)):
        count += 1
    # need to store alot of parts, looking for a smarter way
    prev_k_copy = prev_k
    prev_k,k = k,2*k + prev_k_copy
    prev_j_copy = prev_j
    prev_j,j = j,2*j + prev_j_copy

print count


