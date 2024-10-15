# Explanation:
Imports:
<p>
random: This library is used to select random characters.
string: Provides predefined constants such as ascii_lowercase (lowercase letters), ascii_uppercase (uppercase letters), digits (numbers), and punctuation (special characters).
  
<p>generate_password Function:

<p>Parameters:

<p>length: Specifies the total length of the password (default is 12 characters).
use_uppercase, use_digits, use_special: Boolean values that determine whether to include uppercase letters, digits, and special characters in the password.
Character Sets: The function defines different character sets using string.ascii_lowercase (lowercase letters), string.ascii_uppercase (uppercase letters), string.digits (numbers), and string.punctuation (special characters like @#$%). These sets are combined into all_characters based on the user's choice.
<p>
Error Handling: If no character set is selected, the function raises a ValueError.
<p>
Password Composition:
<p>
The function first ensures the password contains at least one character from each selected set (lowercase, uppercase, digits, special characters).
Then, it fills the remaining length of the password by randomly choosing characters from the all_characters pool.
Finally, the password is shuffled to avoid predictable patterns and returned as a string.
Main Program:
<p>
The script asks the user for input regarding the desired password length and whether to include uppercase letters, digits, and special characters.
It then calls generate_password with these options and prints the generated password.
Usage Example:
  <p>
<code>
Enter the desired password length: 16
Include uppercase letters? (yes/no): yes
Include digits? (yes/no): yes
Include special characters? (yes/no): yes
Generated Password: M9@hB%t3lK!pNc2q
</code>
    <p>
This ensures you get a strong password of the desired length with a good mix of character types, which increases its security against brute-force attacks.
