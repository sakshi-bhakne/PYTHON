text = " Welcome to IMCC!"
#remove spaces
print("Remove Spaces",text.strip())

#capitalize first letter:
text = text.strip()
print("hello sakshi bhakne this side.: ", text.capitalize())

#title case (capitalize each word)
print(text.title())

#count accurances of substring
print(" Letter C occurs ",text.count("C"),"times in text")

#position of substring(-1 , "times in next")
print("position of IMCC in text is ",text.find("IMCC"))

#replace a substring
print(text.replace("IMCC","Python Magic"))

#Check if string starts or ends with certain substring
print(text.startswith(" We"))
print(text.endswith("!"))

#uppercase and lowercase
print("lower case: ",text.lower)
print("uppercase: ",text.upper)