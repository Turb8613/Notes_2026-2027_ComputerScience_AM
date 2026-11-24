def ask_count(character_type):
    while True:
        try:
            count = int(input("How many " + character_type + "? Enter 0 for none: "))
            if count >= 0:
                return count
            print("Enter 0 or a positive number.")
        except ValueError:
            print("Please enter a whole number.")


uppercase = ""
lowercase = ""
numbers = ""
special = "!@#$%^&*()"

for code in range(65, 91):
    uppercase += chr(code)

for code in range(97, 123):
    lowercase += chr(code)

for code in range(48, 58):
    numbers += chr(code)

uppercase_count = ask_count("capital letters")
lowercase_count = ask_count("lowercase letters")
number_count = ask_count("numbers")
special_count = ask_count("special characters")

password = ""

for index in range(uppercase_count):
    position = abs(hash("uppercase" + str(index))) % len(uppercase)
    password += uppercase[position]

for index in range(lowercase_count):
    position = abs(hash("lowercase" + str(index))) % len(lowercase)
    password += lowercase[position]

for index in range(number_count):
    position = abs(hash("number" + str(index))) % len(numbers)
    password += numbers[position]

for index in range(special_count):
    position = abs(hash("special" + str(index))) % len(special)
    password += special[position]

if len(password) == 0:
    print("The password must contain at least one character.")
else:
    seed = str(uppercase_count) + str(lowercase_count) + str(number_count) + str(special_count)
    shuffled_password = ""

    while len(password) > 0:
        position = abs(hash(seed + str(len(shuffled_password)))) % len(password)
        shuffled_password += password[position]
        password = password[:position] + password[position + 1:]

    print("Password:", shuffled_password)
