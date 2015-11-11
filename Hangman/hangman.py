import random

def get_wordlist():
	f=open("/usr/share/dict/words")
	clean_words = []
	for i in f :
		i = i.strip()
		if i.isalpha() and len(i) > 5:
			clean_words.append(i.lower())
	return clean_words

def select_word(wordlist):
	return random.sample(wordlist,1)[0]

def play_hangman(selec_word):
	length = len(selec_word)
        correct_guess = 0
        counter = 0
        letter_list = ["" for i in range(length)]
	while (correct_guess < length and counter < 10) :
                #display the secret word with '*' mark on letters that are not guessed
                # accept a letter
                letter = raw_input()
                # if letter is in secret word, mark it as guessed
                if letter in selec_word :
                        # for correct guess increment correct_guess
                        letter_list[correct_guess] = letter
                        correct_guess = correct_guess + 1
                counter = counter + 1
                
        # if correct_guess equal to length of secret word, success else, hanged
        if (correct_guess == length) :
                return "success"
        else :
                return "You are Hanged"


# main function

word_list = get_wordlist()
secret = select_word(word_list)
result = play_hangman(secret)
print result
