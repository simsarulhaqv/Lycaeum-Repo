# fizzbizz problem

def fizzbizz(number) :
	if (number%15==0):
		return "fizzbizz"
	elif (number%3==0):
		return "fizz"
	elif (number%5==0):
		return "bizz"
	else :
		return number
