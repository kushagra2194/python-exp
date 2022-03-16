word = input("Enter a word:")
bonnie = 0
clyde = 0
vowel = ['a', 'e', 'i', 'o', 'u']

for i in word:
    if i in vowel:
        clyde += 1
    else:
        bonnie +=1

if bonnie > clyde:
    print("Bonnie wins with {0} strings over Clyde who has {1} string.".format(bonnie, clyde))
elif clyde > bonnie:
    print("Clyde wins with {0} strings over Bonnie who has {1} string.".format(clyde, bonnie))
else:
    print("Clyde and Bonnie draw with {0} strings.".format(clyde))