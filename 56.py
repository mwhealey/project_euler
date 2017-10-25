for i in range(1,100):
    # just brute forcing it
    for j in range(1,100):
        print reduce((lambda x, y: int(x)+int(y)), str(i**j))

