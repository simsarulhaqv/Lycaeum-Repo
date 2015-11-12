# Find panagram

def panagram(input_string) :
	for i in "abcdefghijklmnopqrstuvwxyz" :
		if(i not in input_string):
			return False
	return True


