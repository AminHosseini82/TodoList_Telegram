import bcrypt

def hash_password(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Generate a salt (random string)
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    # Decode the hashed password back to a string for storage
    return hashed_password.decode('utf-8')

# Example usage
plain_password = "******"
hashed_pw = hash_password(plain_password)
print(plain_password)
print(f"Hashed Password: {hashed_pw}")