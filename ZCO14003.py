# def profit(arr):
#     length = len(arr)
#     max = arr[0]
#     for i in range(length):
#         if i < length-1:
#             # if i != 0:
#             print(arr[i], max, arr[i+1]*(i+2), i)
#             if max < arr[i+1]*(i+2):
#                 max = arr[i+1]*(i+2)
#     return max

arr = []
mx = 0
for t in range(int(input())):
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
# print(profit(arr))

for i in range(len(arr)):
    mx = max(mx, arr[i]*(i+1))
print(mx)