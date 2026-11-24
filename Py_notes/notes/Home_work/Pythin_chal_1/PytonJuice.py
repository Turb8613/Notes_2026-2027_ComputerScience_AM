def bottle_word(count):
    if count == 1:
        return "bottle"
    return "bottles"


for count in range(99, 0, -1):
    print(f"{count} {bottle_word(count)} of Python Juice on the wall,")
    print(f"{count} {bottle_word(count)} of Python Juice.")

    if count == 1:
        print("Take it down and pass it around,")
        print("no more bottles of Python Juice on the wall.")
    else:
        next_count = count - 1
        print("Take one down and pass it around,")
        print(f"{next_count} {bottle_word(next_count)} of Python Juice on the wall.")

    print()

print("No more bottles of Python Juice on the wall,")
print("no more bottles of Python Juice.")
print("Go to the store and buy some more,")
print("99 bottles of Python Juice on the wall.")