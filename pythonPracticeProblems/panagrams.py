# Find panagram

def panagram(input_string) :
	for i in "abcdefghijklmnopqrstuvwxyz" :
		if(i not in input_string):
			return False
	return True


# adding test cases

result = panagram("This is meow")
print result # expected output False

result = panagram("The quick brown fox jumps over the lazy dog") 
print result # expected output True
