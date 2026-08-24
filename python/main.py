# BCH Software Inc. - Sprint 1: Interactive Kiosk
# Track: Python Software Engineering
#824

def main():
    print("========================================")
    print("      BCH ENTERPRISE VISITOR KIOSK      ")
    print("========================================")
    
    # SE: Use input() to capture Name, Company, Email, and Badge Tier
    # SE: Use print() to render the ASCII badge

if __name__ == "__main__":
    main()
    # Pseudocode: prompt user for input

# 1. Display a message asking the user for information
# 2. Wait for the user to type something and press Enter
# 3. Store what they typed in a variable
# 4. (Optional) Convert the input to the right type (int, float, etc.)
# 5. (Optional) Validate the input (check it's not empty, is a number, in range, etc.)
# 6. Use the input value in the rest of the program
 # Basic prompt
name = input("Enter your name: ")

# Prompt expecting a number
age = int(input("Enter your age: "))

# Prompt with validation
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number.")

# Use it
print(f"Hello, {name}! You are {age} years old.")