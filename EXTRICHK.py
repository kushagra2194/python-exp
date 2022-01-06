def extrichk(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        if a == b == c:
            return 1
        elif a == b or b == c or a == c:
            return 2
        else:
            return 3
    else:
        return "-1"

a, b, c = map(int,input().split())
print(extrichk(a, b, c))
