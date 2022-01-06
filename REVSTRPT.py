def revstrpt(n):
    for i in range(1, n+1):
        blanks = n - i
        for a in range(blanks):
            print(" ", end ="")
        for a in range(i):
            # print(a, i)
            if a == i-1:
                print("*")
            else:
                print("*", end ="")

n = int(input())
revstrpt(n)
