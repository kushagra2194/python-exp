factor = []
def print_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            factor.append(i)
    print(len(factor))
    for i in factor:
        print(i, end =" ")

n = int(input())
print_factors(n)
