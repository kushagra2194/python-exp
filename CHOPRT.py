for t in range(int(input())):
    n = input()
    x, y= map(int,n.split())
    if x < y:
        print("<")
    elif x > y:
        print(">")
    elif x == y:
        print("=")