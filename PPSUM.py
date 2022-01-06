for t in range(int(input())):
    n = input()
    x, y= map(int,n.split())
    total = 0
    for i in range(x):
        total=y*(y+1)/2
        y=total
    print(int(total))
