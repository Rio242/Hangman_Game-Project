#Step 1 

#word_list = ["aardvarka", "baboon", "camel", "lover", "mango"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
from hangman_words import word_list
from hangman_art import stages
import random

#function to select random word from list above 
chosen_word = random.choice(word_list)
print(f'The chosen word is:{chosen_word}')
#Below is what I would you in a loop and unspecified number of entries in list 
#num_words =  len(word_list)-1 

#random_word = random.randint(0,num_words)
#chosen_word = word_list.pop(random_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# for lop to generate list with blanks from chosen word 
blank_word = []
for b in chosen_word:
    blank_word.append('_')
print(blank_word)

#convert word string to its own list
chosenword_list = list(chosen_word)
#print(chosenword_list)

#while loop 
art = 0
lives = 6
while (blank_word != chosenword_list): 
    
#input to ask user to guess
    user = input("Please guess a letter").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#Mario- user gets 6 attempts 


# for loop to check if guessed letter matches in word. Then if statement is included to replace the blank with letter if correct  

    
    wrong = 0
    #for n in chosen_word
    for n in range(len(chosenword_list)):
        
        if chosenword_list[n] == user:#if n ==user
            #location = chosenword_list.index(n)
           blank_word[n] = user #blank_word[location] = user
            #print("")
        else:
            wrong += 1    
            #print("Wrong")
    #if statement to keep track of lives 
          
    if wrong == len(chosen_word):
        lives -=1 
        print(f"Wrong")
        art += 1
        print(stages[art])
        
        
        if lives == 0:
            break
            
    print(blank_word) # stays
    
if blank_word == chosenword_list:

    print("You won")
elif lives == 0:
    print("Game over, you ran out of lives ")
        
