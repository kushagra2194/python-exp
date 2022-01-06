def revmee(a, n):
    arr = n.split()
    arr1 = [ele for ele in reversed(arr)]
    b = " "
    # for i in arr:
    #     arr1.reverse
    return b.join(arr1)

a = input()
n = input()
print(revmee(a, n))
