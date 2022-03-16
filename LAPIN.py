def lapin(words):
    for i in words:
        l = len(i)
        half = int(l/2)
        a = sorted(i[half:]) if l%2==0 else sorted(i[half+1:])
        b = sorted(i[:half]) 
        print("YES" if a == b else "NO")
            

words = []

for t in range(int(input())):
    n = input()
    words.append(n)
    
lapin(words)