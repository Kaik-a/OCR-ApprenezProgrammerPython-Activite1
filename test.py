import hashlib
    
print(hashlib.algorithms_guaranteed)
    
print(hashlib.algorithms_available)

password = hashlib.sha1(b"password")

print(password.digest())

print(password.hexdigest())