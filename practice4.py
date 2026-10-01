n = int(input("Enter the number of elements: "))

arr = []

for i in range (n):
    arr.append(int(input("Enter the number : ")))

    search = (int(input("number to search : ")))

    if search in arr:
        print("number is present. ")
        print("position = ",arr.index(search) + 1)
    else:
        print("number is not present.")