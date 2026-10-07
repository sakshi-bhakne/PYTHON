# n = input("enter any sentence: ")
# print(" count : ",n.count("a","e","i","o","u",))

# n = input("Enter any sentence: ")

# count = sum(n.count(vowel) for vowel in "aeiou")

# print("Count:", count)

#sec method:
# n = input("Enter any sentence: ")

# print("Count:", n.count("a") + n.count("e") + n.count("i") + n.count("o") + n.count("u"))

# name = input("enter your name: ")
# print("letter s occurence",name.count("s"),"times in text")

# name = input("enter your name: ")
# print("replace s ",name.replace("s","z"))

# name = input("enter your name: ")
# print("split the name :",name.split())

#empty list
my_list = []
print (my_list)

#with items
fruits = ["apple","mango","banana"]
print(fruits)

#to access any element use index
numbers = [10,20,30,40]
print(numbers[0])
print(numbers[-2])

#append item in list
color = ["red","green"]
color.append("black")
print(color)


#insert at specific location

color = ["red","green"]
color.insert("black")
print(color)

#Functions:

#length
numbers = [1,2,3,4,5,6,7]
print(len(numbers))


#sum
numbers = [1,2,3,4,5,6,7]
print(sum(numbers))


#sorting
numbers = [1,2,3,4,5,6,7]
print(sorted(numbers))
print(sorted(numbers,reverse=True))

