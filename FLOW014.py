def gradeCheck(h,c,s):
    if h > 50 and c < 0.7 and s > 5600:
        return(10)
    elif h > 50 and c < 0.7:
        return(9)
    if c < 0.7 and s > 5600:
        return(8)
    if h > 50 and s > 5600:
        return(7)
    if h > 50 or c < 0.7 or s > 5600:
        return(6)
    if not h > 50 and not c < 0.7 and not s > 5600:
        return(5)

for t in range(int(input())):
    n = input()
    h, c, s = map(float,n.split())
    print(gradeCheck(h,c,s))
