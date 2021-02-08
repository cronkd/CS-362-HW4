#Function to get volume of cube
def volume(l):
	#check if input is a float
	try:
		floatL = float(l)
	#if not, return error
	except ValueError:
		return -1
	#if length is negative, return error
	if l <= 0:
		return -1
	#Find and return volume
	vol = l*l*l
	return vol
			
	
