from Crypto.PublicKey import RSA

with open('bruce_rsa.pub','rb') as f:
    key = RSA.import_key(f.read())

print(key.n)