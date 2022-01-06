def if_triangle(a, b, c):
    if 0 < a < 180 and 0 < b < 180 and 0 < c < 180:
        if a + b + c == 180:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

n = input()
a, b, c = map(int,n.split())
print(if_triangle(a, b, c))
