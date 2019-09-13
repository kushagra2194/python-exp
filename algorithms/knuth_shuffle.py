import random

def shuffle(a):
	for i in range(len(a)-1,0,-1):
		j = random.randint(0,i)
		c = a[i]
		a[i] = a[j]
		a[j] = c
	return a

arr = [1,2,3,4,5]
print shuffle(arr)
