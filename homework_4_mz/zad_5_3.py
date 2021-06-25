import string
import os

d = dict()



file = open("pan_tadeusz_2.txt")
lines = file.readlines()

for line in lines:
	line = line.strip()
	line = line.lower()
	line = line.translate(line.maketrans("", "", string.punctuation))

	words = line.split(" ")

	for word in words:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1



count_words = 0
count_symbols = 0
special_chars = "!@#$%^&*()-+?_=,<>/"
for key in d:
	if key in special_chars:
		count_symbols += 1
	else:
		count_words += 1

print(d)
print(len(d))
print(count_symbols)
print(count_words)













