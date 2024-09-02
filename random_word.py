import random
value=True
while(value):
#List of words to choose from
    word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
    selected_word = random.choice(word_list)
# Initialize the user's guess
    user_guess = ""
