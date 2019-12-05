for t in range(int(input())):
	n = input().split()
	arr = list(map(int, n))
	arr.sort()
	# i =	 arr[0]/2

	def hcf(a,b): 
		if(b==0): 
			return a 
		else: 
			return hcf(b, a%b)   
	# while i > 0:
	# 	if arr[0] % i == 0 and arr[1] % i == 0:
	# 		hcf = i
	# 		break
	# 	i -= 1
	hcf = hcf(arr[0] , arr[1])
	lcm = int(arr[0] * arr[1] / hcf)
	print(str(hcf) + " " + str(lcm))