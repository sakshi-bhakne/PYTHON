#2.Print all unique words.
f = open("data.txt", "r")

content = f.read()
words = content.split()

unique_words = set(words)

print("Unique words:", unique_words)

f.close()