def rectangle(a,b,c,d):
    if a == b and c == d :
        return("YES")
    elif a == c and b == d :
        return("YES")
    elif a == d and b == c :
        return("YES")
    else:
        return("NO")

for t in range(int(input())):
    a, b, c, d = map(int,input().split())
    print(rectangle(a,b,c,d))
