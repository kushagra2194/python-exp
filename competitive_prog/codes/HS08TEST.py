n = input().split()
arr = list(map(float, n))
if arr[0]%5 == 0 and arr[0] <= arr[1]-0.50:
	print("%.2f" % (arr[1]-arr[0]-0.50))
else:
	print("%.2f" % arr[1])