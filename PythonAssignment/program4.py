#Que4:Read a file, split its content into words, and store them in a list.
#1.Print the total number of words.

f = open("data.txt", "r")

content = f.read()
words = content.split()

print("Total words:", len(words))

f.close()