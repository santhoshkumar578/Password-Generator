import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Minimum is 4 characters."
    else:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        for _ in range(length - 4):
            password.append(random.choice(all_characters))
        random.shuffle(password)
        return ''.join(password)

length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(length))
