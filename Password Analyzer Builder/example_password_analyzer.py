import re

def check_password_strength(password):
    strength = 0
    # Length check
    if len(password) >= 12:
        strength += 1
    
    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Numbers check
    if re.search(r'[0-9]', password):
        strength += 1
    
    # Special character check
    if re.search(r'[!@#$%^&*()]', password):
        strength += 1
    
    # Return strength out of 5
    return strength

password = input("Enter your password: ")

strength = check_password_strength(password)
print(f"Password Strength: {strength}/5")
if strength < 3:
    print("Your password is weak. Consider making it longer and using a mix of upper and lower case letters, numbers, and special characters.")
elif strength < 5:
    print("Your password is moderate. You could improve it by adding more variety.")
else:
    print("Your password is strong. Good job!")

# Add this line to keep the window open
input("Press Enter to exit...")