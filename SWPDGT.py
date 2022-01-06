def sum(a,b):
    sum = a + b
    arr1 = [int(d) for d in str(a)]
    arr2 = [int(d) for d in str(b)]
    arr = arr1 +arr2
    arr.sort(reverse=True)
    print(arr)
    a = ""
    b = ""
    for i in range(len(arr)):
        a = a + arr[i]
    new_sum = int(arr[0]+arr[1]) + int(arr[2]+arr[3])
    if new_sum > sum:
        sum = new_sum
    return(sum)
        

for t in range(int(input())):
    a, b = map(int,input().split())
    print(sum(a,b))
