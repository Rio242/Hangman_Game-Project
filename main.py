#Step 1 

word_list = ["aardvarka", "baboon", "camel", "lover", "mango"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
chosen_word= random.choice(word_list)
print(chosen_word)
#Below is what I would you in a loop and unspecified number of entries in list 
#num_words =  len(word_list)-1 

#random_word = random.randint(0,num_words)
#chosen_word = word_list.pop(random_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

user = input("Please guess a letter").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#Mario- user gets 6 attempts 
# for loop 
for n in chosen_word:
    
    if n == user:
        print("Right")
    else:
        print("Wrong")
