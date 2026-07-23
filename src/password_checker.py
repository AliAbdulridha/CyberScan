import string

def password_checker():
    
    password = input("Enter a password: ") 

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    long_enough = len(password) >= 8 

    score = 0

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if long_enough:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\nPassword Analysis")
    print("-----------------")
    print(f"Strength: {strength}")
    print(f"Score: {score}/5")