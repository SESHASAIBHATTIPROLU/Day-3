def comb(L):
    n=int(input("enter the range of combination :"))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])
comb([1,0,0,1])
