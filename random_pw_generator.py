#build a program that intakes some words from the user 
# then generates a random password using those words. 
import random 

word = input("Enter a word you will remember (the longer the better!): ")
new_list = list(word)
random.shuffle(new_list)
final_list = ''.join(new_list)
print(final_list)
