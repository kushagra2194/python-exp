def expense(a,b):
    cost = a * b
    if a > 1000:
        return(cost - cost*10/100)
    else:
        return(cost)
        

for t in range(int(input())):
    a, b = map(int,input().split())
    print(expense(a,b))
