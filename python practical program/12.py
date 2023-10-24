#practical no.12
#Program to read a file and capitalize the first letter of every word in the file.

result = ""
file_gfg = open('temp.txt', 'r')
for line in file_gfg:
	g = line.split()
	for elem in g:
		# capitalize first letter of each word and add to a string
		if len(result) > 0:
			result = result + " " + elem.strip().capitalize()
		else:
			result = elem.capitalize()

print(result)
