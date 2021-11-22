from Crypto.PublicKey import RSA

with open('2048b-rsa-example-cert','rb') as f:
    key = RSA.import_key(f.read())

print(f"RSA certificate modulus: {key.n}")