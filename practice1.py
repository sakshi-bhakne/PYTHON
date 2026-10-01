
n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
  num = int(input("Enter a number: "))
  arr.append(num)

sum = 0 

for num in arr:
  sum = sum + num 
  print("sum = ",sum)
