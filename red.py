for i in range(1,2):
    for n in range(1,6):
        for j in range(n-1,0,-1):
            print(" ",end="")
        for j in range(1,7-n):
            print(j,end="")
        for j in range(5-n,0,-1):
            print(j,end="")
        print()
    for p in range(2,6):
        for s in range(p,5):
            print(" ",end="")
        for s in range(p,0,-1):
            print(s,end="")
        for s in range(2,p+1):
            print(s,end="")
        print()
    print()

