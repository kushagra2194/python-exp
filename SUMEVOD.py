def sumevod(n):
    n = n*2
    t_odd = 0
    t_even = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            t_even = t_even + i
        else:
            t_odd = t_odd + i
    print("{0} {1}".format(t_odd, t_even))
        

n = int(input())
sumevod(n)
