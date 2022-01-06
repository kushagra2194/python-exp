def findmeli(b, n):
    arr = n.split()
    if b in arr:
        return 1
    else:
        return -1

a, b = map(str,input().split())
n = input()
print(findmeli(b, n))
