numbers = [10, 20, 30, 40, 50]
n = int(input("Enter a number to search:"))

for i in numbers:
    if i == n:
        print("Number found")
        break
else:
    print("Number not found")
    