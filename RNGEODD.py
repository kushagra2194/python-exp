def expense(l, r):
    for i in range(l, r+1):
        if not i % 2 == 0:
            print(i, end =" ")

n = input()
l, r = map(int,n.split())
expense(l, r)
