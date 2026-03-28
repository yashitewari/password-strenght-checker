import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*]", password):
        strength += 1

    if strength <= 2:
        return "Weak ❌"
    elif strength == 3:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

def main():
    print("=== Password Strength Checker ===")

    while True:
        password = input("\nEnter a password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Goodbye!")
            break

        result = check_password_strength(password)
        print(f"Strength: {result}")

if __name__ == "__main__":
    main()
