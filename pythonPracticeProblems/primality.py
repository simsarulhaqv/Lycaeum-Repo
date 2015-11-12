# Primality 

# modify size to change list length
size = 100
# initialize list with zeroes
x = [0 for x in range(101)]

# primality function
def primality(number) :
    if (number not in x) :
        value = number
        counter = 1
        while(value <= 100) :
            value = counter*number
            x[value] = value 
            counter = counter + 1
        return number
    else :	
        return "NIL",count


number = input("range ")
for i in range(2,number):
	ans=primality(i)
	if ( ans != "NIL") :
 		print ans
