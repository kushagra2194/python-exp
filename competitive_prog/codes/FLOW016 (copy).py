for t in range(int(input())):
	n = input().split()
	arr = list(map(int, n))
	arr.sort()
	i =	 arr[0]/2
	while i > 0:
		if arr[0] % i == 0 and arr[1] % i == 0:
			hcf = i
			break
		i -= 1
	lcm = str(int(arr[0] * arr[1] / hcf))
	hcf = str(i)
	print(hcf + " " + lcm)