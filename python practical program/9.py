#practical no.9
"""Program to create a dictionary with key as first character and value as words
starting with that character."""

string_input = input("enter the string:")

words = string_input.split()
  
dictionary = {}
  
for word in words:
  

    if (word[0] not in dictionary.keys()):
        dictionary[word[0]] = []
        dictionary[word[0]].append(word)
  
    
    else: 
        if (word not in dictionary[word[0]]):
            dictionary[word[0]].append(word)
  

print(dictionary)
