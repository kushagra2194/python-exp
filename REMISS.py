for t in range(int(input())):
    n = input()
    x, y= map(int,n.split())
    print(str(x if x>y else y) + " " + str(x+y))