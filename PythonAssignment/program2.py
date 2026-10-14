#Que2.Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.

f = open("data.txt","r")

lines = f.readlines()

print("Total lines:", len(lines))
print("2nd line:", lines[2])
print("4th line:", lines[3])

f.close()
