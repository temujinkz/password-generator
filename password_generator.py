import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets based on user preferences
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    # Combine all selected character sets
    all_characters = lowercase + uppercase + digits + special
    
    if not all_characters:
        raise ValueError("At least one character set must be selected.")
    
    # Ensure the generated password includes characters from all selected sets
    password = [
        random.choice(lowercase),
        random.choice(uppercase) if use_uppercase else '',
        random.choice(digits) if use_digits else '',
        random.choice(special) if use_special else ''
    ]
    
    # Fill the remaining length of the password with random characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle to make the password unpredictable
    random.shuffle(password)
    
    # Convert the list to a string and return the password
    return ''.join(password)

if __name__ == "__main__":
    # User inputs for password length and character set options
    password_length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    # Generate and print the password
    password = generate_password(length=password_length, use_uppercase=include_uppercase, use_digits=include_digits, use_special=include_special)
    print(f"Generated Password: {password}")
