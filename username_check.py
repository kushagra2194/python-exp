import re 

def username_check(username):
	flag = 0
	while True:   
	    if (len(username)<6): 
		flag = -1
		break
	    elif not re.search("[a-z]", username): 
		flag = -1
		break
	    elif not re.search("[A-Z]", username): 
		flag = -1
		break
	    elif not re.search("[0-9]", username): 
		flag = -1
		break
	    elif re.search("[_@$]", username): 
		flag = -1
		break
	    elif re.search("\s", username): 
		flag = -1
		break
	    else: 
		flag = 0
		print("Valid Password") 
		print(username) 
		break
	  
	if flag ==-1: 
	    print("Not a Valid username") 

username_check("TestUsername123")
