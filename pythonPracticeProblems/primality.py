# Primality

x = [0 for x in range(100)]

def primality(number,count) :
	for index in x:
		if (index != 0) :
			if (number % index) == 0 :
				return "NIL",count
	else :	
		x[count] = number
		count = count + 1		
		return number,count


