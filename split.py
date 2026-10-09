a = [10, "Sakshi",20,30,"sujal",25,26,35,"sampada",]

numbers = []
names = []

for i in a:
    if type(i) == int:
        numbers.append(i)
    else:
        names.append(i)
print("Numbers:", numbers)
print("Names:", names)
print("Highest number:", max(numbers))


