import re 

def pass_strength(password):
	flag = 0
	while True:   
	    if (len(password)>6): 
		flag += 1
	    if re.search("[a-z]", password): 
		flag += 1
	    if re.search("[A-Z]", password): 
		flag += 1
	    if re.search("[0-9]", password): 
		flag += 1
	    if re.search("[_@$]", password): 
		flag += 2
	    if re.search("\s", password): 
		flag = -1
		break
	    else: 
		# flag = 0
		print("Valid Password") 
		print("flag : ", flag) 
		if flag == 0:
			print("Not a Valid Password")
		elif flag <= 3:
			print("Medium Password")
		elif flag <= 6:
			print("Strong Password")
		break
	  
	if flag ==-1: 
	    print("Not a Valid Password") 

pass_strength("Thi$i$@te$t123")
