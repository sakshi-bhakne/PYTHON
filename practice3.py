n = int(input("Enter number : "))

arr =[]

for i in range(n):
    arr.append(int(input("enter the number : ")))
    
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even = even + 1
    else :

        odd = odd + 1

    print("Even number = ",even)
    print ("Odd number = ",odd)