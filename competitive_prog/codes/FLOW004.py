n = int(input())
for i in range(n):
	num = int(input())
	first = int(str(num)[:1])
	last = num%10
	print(first+last)