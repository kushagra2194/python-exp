# fact = []
# for t in range(int(input())):
#     n = int(input())
#     l = 0
#     while n > 0:
#         if l == 0:
#             l = n
#         else:
#             l = l * n
#         n-=1
#     fact.append(l)
# for i in fact:
#     print(i)

def fact(n):
    if n==1 or n==0:
        return 1
    result=1
    result*=fact(n-1)
    return n*result
t=int(input())
for i in range(0,t):
    m=int(input())
    print(fact(m))