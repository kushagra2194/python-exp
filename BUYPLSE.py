def expense(a, b, x, y):
    return a*x+b*y

n = input()
a, b, x, y = map(int,n.split())
print(expense(a, b, x, y))
