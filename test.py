import bcrypt

# 1. Hashing a password
password = b"mysecretpassword"  # Passwords must be bytes
salt = bcrypt.gensalt()  # Generate a random salt
hashed_password = bcrypt.hashpw(password, salt)

print(f"Original password: {password.decode()}")
print(f"Generated salt: {salt}")
print(f"Hashed password: {hashed_password}")

# 2. Verifying a password
user_input_password = b"mysecretpword"  # User provides password as bytes

if bcrypt.checkpw(user_input_password, hashed_password):
    print("Password matches!")
else:
    print("Password does not match.")

# Example with an incorrect password
incorrect_password = b"wrongpassword"
if bcrypt.checkpw(incorrect_password, hashed_password):
    print("This should not print.")
else:
    print("Incorrect password entered.")