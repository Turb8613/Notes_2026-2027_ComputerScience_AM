fruits = ["apples", "bananas"]

lyrics = (
    ("I like to eat, eat, eat apples and bananas", ""),
    ("I like ate, ate, ate epples and benenes", ""),
    ("I like to eat, eat, eat eepples and beeneenees", ""),
    ("I like to ite, ite, ite ipples and bininis", "And "),
    ("I like to ote, ote, ote, oplles and bononos", ""),
    ("I like to ute, ute, ute upples and bununus", "And ")
)

print("Fruits:", ", ".join(fruits))

for line, opening in lyrics:
    print(opening + line)
    print(line)
