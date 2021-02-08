#Function for joining first and last name. Takes in two strings
def first_last(x,y):
	#If first name empty, return -1 (error)
	if x == '':
		return -1
	#for every character in first name, if there is a number, return -1
	for i in x:
		if i.isdigit():
			return -1
	#same error handling for last name y
	if y == '':
		return -1
	for j in y:
		if j.isdigit():
			return -1
	#add last name to first
	x += y
	#return full name
	return x
