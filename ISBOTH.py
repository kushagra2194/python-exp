def isboth(n):
    if n % 5 == 0 and n % 11 == 0:
        return "BOTH"
    elif n % 5 == 0 or n % 11 == 0:
        return "ONE"
    else:
        return "NONE"

n = int(input())
print(isboth(n))
