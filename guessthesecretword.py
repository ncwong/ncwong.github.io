import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

print ("Your word is " + str(len(word)) + " letters long.")

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_", "_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
	if not (guess.isalpha() and len(guess) == 1 and guess.islower()):
		print ("Your guess needs to be a single lower case letter.")
	elif guess in word:
		print ("correct")
		
	elif guess in guesses:
		print ("You already guessed that letter. Try again")
	else:
		print ("That letter is not in your word. Try again")


	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
