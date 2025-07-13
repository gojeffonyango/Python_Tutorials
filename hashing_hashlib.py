import hashlib

# Example of SHA-256 hashing
data = "Hello, World!".encode()  # Convert string to bytes
hash_object = hashlib.sha256(data)
hashed_data = hash_object.hexdigest()
print(f"SHA-256 Hash: {hashed_data}")
