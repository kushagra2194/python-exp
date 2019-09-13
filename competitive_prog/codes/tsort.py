num = int(input())
list = []
for i in range(num):
	n = int(input())
	list.append(n)
list.sort()
for i in list:
	print(i)