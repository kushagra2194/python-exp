def gradeCheck(n):
    if n % 10 == 0:
        return(0)
    elif n % 5 == 0:
        return(1)
    else:
        return(-1)

for t in range(int(input())):
    n = int(input())
    print(gradeCheck(n))
