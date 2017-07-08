#Assignment: Find Characters
#Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.




word_list = ['hello','world','my','name','is','Anna']

char = str('o')

new_list = ""

for new_list in word_list:
        if new_list.find(char) != -1:
            print new_list

#results = word_list.split(',')
