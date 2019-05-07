for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i + j + k < 2:
                print(i,j,k)
            print(k)
        print(j)
    print(i)
