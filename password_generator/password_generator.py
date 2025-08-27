import random
import string

def generate_password(length, complexity):
    characters = ""

    # Define complexity levels
    if complexity == 1:
        characters = string.ascii_lowercase   # only lowercase letters
    elif complexity == 2:
        characters = string.ascii_letters     # upper + lowercase letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits  # letters + numbers
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation  # full set
    else:
        print("Invalid choice! Defaulting to complexity level 4.")
        characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- Main Program ---
print("🔑 Password Generator 🔑")
length = int(input("Enter desired password length: "))
print("Select complexity level:")
print("1 - Lowercase only")
print("2 - Uppercase + Lowercase")
print("3 - Letters + Numbers")
print("4 - Letters + Numbers + Symbols")

complexity = int(input("Enter choice (1-4): "))

# Generate and show password
password = generate_password(length, complexity)
print("\n✅ Generated Password:", password)
