def valtri(n):
    if n % 5 == 0 or n % 6 == 0:
        return("YES")
    else:
        return("NO")

n = int(input())
print(valtri(n))
