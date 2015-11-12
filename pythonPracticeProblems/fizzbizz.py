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

# testing for numbers from 1 to 50

for i in range(1,51):
	output=fizzbizz(i)
	print output
