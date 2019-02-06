import re 

def pass_validate(password):
	flag = 0
	while True:   
	    if (len(password)<6): 
		flag = -1
		break
	    elif not re.search("[a-z]", password): 
		flag = -1
		break
	    elif not re.search("[A-Z]", password): 
		flag = -1
		break
	    elif not re.search("[0-9]", password): 
		flag = -1
		break
	    elif not re.search("[_@$]", password): 
		flag = -1
		break
	    elif re.search("\s", password): 
		flag = -1
		break
	    else: 
		flag = 0
		print("Valid Password") 
		print(password) 
		break
	  
	if flag ==-1: 
	    print("Not a Valid Password") 

pass_validate("Thi$i$@te$t")
