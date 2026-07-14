import random
import string
 
while True:
    while True:
        try:
            length = int(input("Enter Password Length (Minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    upper = input("Include Uppercase? (y/n): ").lower()
    lower = input("Include Lowercase (y/n): ").lower()
    digits = input("Include Numbers (y/n): ").lower()
    symbols = input("Include Symbols (y/n): ").lower()

    character = ""
    password = []
    if upper == "y" :
                 character += string.ascii_uppercase 
                 password.append(random.choice(string.ascii_uppercase)) 
        
    if lower == "y" :
                character += string.ascii_lowercase
                password.append(random.choice(string.ascii_lowercase)) 
        
    if digits == "y" :
                character += string.digits 
                password.append(random.choice(string.digits)) 
        
    if symbols == "y" :
                character += string.punctuation     
                password.append(random.choice(string.punctuation)) 
        
    count = 0 
    if upper == "y":
            count += 1
    if lower == "y":
            count += 1
    if digits == "y":
            count += 1
    if symbols == "y":
            count += 1 
    if count < 2:
                print("Please select at least two character types.")
                continue
    while len(password) < length:
            password.append(random.choice(character))

    random.shuffle(password)

    print("Generated Password:" )
    print("".join(password))

    again = input("\nGenerate another password? (y/n): ").lower()

    if again != "y":
        print("Thank you for using Password Generator.")
        break