import itertools

while True:
    n=input().split()
    temp=map(int,n[1:])
    k=int(n[0])
    if k==0:
        break
    case=itertools.combinations(temp,6)
    for i in case:
        print(*i)
    print()
