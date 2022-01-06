def salaryCheck(n):
    if n < 1500:
        hra = n *10/100
        da = n *90/100
    else:
        hra = 500
        da = n *98/100
    salary = n + hra + da
    return salary

for t in range(int(input())):
    n = int(input())
    print(salaryCheck(n))
