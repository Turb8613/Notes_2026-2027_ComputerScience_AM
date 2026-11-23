height = int(input("Enter the height: "))

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
