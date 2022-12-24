def fact(n):
    
    if n in [0,1]:
        return 1
    else:
        print(n * fact(n-1))
        return n * fact(n-1)



fact(3)