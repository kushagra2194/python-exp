def trivalch(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return "YES"
    else:
        return "NO"

a, b, c = map(int,input().split())
print(trivalch(a, b, c))
