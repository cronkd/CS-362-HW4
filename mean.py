#Function to return average of list, with input as list
def avg(array):
	#if array is empty, return -1
	if not array:
		return -1
	#For every value in array, check if float. If not, return error
	for x in array:
		try: 
			float(x)
		except ValueError:
			return -1
	#return average
	return sum(array)/len(array)

