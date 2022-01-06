def if_triangle(a, b, c):
    if a+b+c == 180:
        return "YES"
    else:
        return "NO"

for t in range(int(input())):
    n = input()
    a, b, c = map(int,n.split())
    print(if_triangle(a, b, c))
