for i in range(int(input())):
	n = int(input())
	arr = input().split()
	arr = list(map(int, arr))
	arr.sort()
	sum = arr[0] + arr[1]
	print(sum)

	# for j in range(n - 1):
	# 	num = str(input())
	# 	arr = num.split()
	# 	arr = list(map(int, arr))
	# 	arr.sort()
	# 	print(arr[0], arr[1])
	# 	sum = arr[0] + arr[1]
	# 	print(sum)