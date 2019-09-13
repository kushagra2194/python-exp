num = int(input())

for i in range(num):
	n = input()
	list = [int(x) for x in str(n)]
	mysum = sum(list)
	print(mysum)