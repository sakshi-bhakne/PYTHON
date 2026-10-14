#Que3:Take a sentence from the user, split it into words, and store them in a list. Print the longest word.
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)