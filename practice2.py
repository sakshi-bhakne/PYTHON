n = int(input("Enter n: "))

a = []

for i in range(n):
    a.append(int(input("Enter number: ")))

a.sort()

print("Smallest =", a[0])
print("Second Smallest =", a[1])
print("Largest =", a[n-1])
print("Second Largest =", a[n-2])