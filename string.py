# Ask user name
name = input("What's your name? ").strip().title()

# Slipt user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {last}")