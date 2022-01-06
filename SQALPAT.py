def sqalpat(n):
    arr = []
    a = " "
    for i in range(1, n*5+1):
        if i % 10 == 0:
            arr.append(str(i))
            arr1 = [ele for ele in reversed(arr)]
            print(a.join(arr1))
            arr = []
        elif i % 5 == 0:
            arr.append(str(i))
            print(a.join(arr))
            arr = []
        else:
            arr.append(str(i))
            # print(i, end=' ')

n = int(input())
sqalpat(n)
