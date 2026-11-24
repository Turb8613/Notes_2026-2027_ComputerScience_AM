height = int(input("Enter the height: "))

for row in range(height):
    spaces = height - row - 1
    blocks = row + 1
    print(" " * spaces + "*" * blocks + " " + "*" * blocks)
