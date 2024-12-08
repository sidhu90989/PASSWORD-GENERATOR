import random
import string

class PasswordGenerator:
    def __init__(self):
        """
        Initialize password character sets
        """
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = string.punctuation

    def generate_password(self, length=12, use_uppercase=True, 
                           use_digits=True, use_special_chars=True):
        """
        Generate a secure password with customizable complexity
        
        :param length: Total length of the password
        :param use_uppercase: Include uppercase letters
        :param use_digits: Include numeric digits
        :param use_special_chars: Include special characters
        :return: Generated password string
        """
        # Validate password length
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")

        # Determine character set based on complexity options
        character_set = self.lowercase
        if use_uppercase:
            character_set += self.uppercase
        if use_digits:
            character_set += self.digits
        if use_special_chars:
            character_set += self.special_chars

        # Ensure at least one character from each selected category
        password = []
        if use_uppercase:
            password.append(random.choice(self.uppercase))
        if use_digits:
            password.append(random.choice(self.digits))
        if use_special_chars:
            password.append(random.choice(self.special_chars))

        # Fill the rest of the password with random characters
        while len(password) < length:
            password.append(random.choice(character_set))

        # Shuffle the password to randomize character positions
        random.shuffle(password)

        # Convert list to string
        return ''.join(password)

    def generate_multiple_passwords(self, count=5, length=12, 
                                     use_uppercase=True, 
                                     use_digits=True, 
                                     use_special_chars=True):
        """
        Generate multiple unique passwords
        
        :param count: Number of passwords to generate
        :param length: Length of each password
        :param use_uppercase: Include uppercase letters
        :param use_digits: Include numeric digits
        :param use_special_chars: Include special characters
        :return: List of generated passwords
        """
        passwords = set()
        while len(passwords) < count:
            passwords.add(
                self.generate_password(
                    length, 
                    use_uppercase, 
                    use_digits, 
                    use_special_chars
                )
            )
        return list(passwords)

def main():
    """
    Main function to run the password generator application
    """
    print("🔐 Secure Password Generator 🔐")
    
    generator = PasswordGenerator()

    while True:
        try:
            # Password length input
            length = int(input("\nEnter desired password length (minimum 4): "))
            if length < 4:
                print("Password must be at least 4 characters long!")
                continue

            # Complexity options
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
            use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

            # Number of passwords to generate
            num_passwords = int(input("How many passwords do you want to generate? "))

            # Generate passwords
            passwords = generator.generate_multiple_passwords(
                count=num_passwords,
                length=length,
                use_uppercase=use_uppercase,
                use_digits=use_digits,
                use_special_chars=use_special_chars
            )

            # Display generated passwords
            print("\n🔑 Generated Passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"{i}. {password}")

            # Continue or exit
            another = input("\nGenerate more passwords? (yes/no): ").lower()
            if another != 'yes':
                print("Thank you for using the Password Generator!")
                break

        except ValueError as e:
            print(f"Error: {e}. Please enter valid inputs.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()