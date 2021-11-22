from Crypto.PublicKey import RSA

KEY="privacy_enhanced_mail.pem"

with open(KEY,"r") as f:
    tmp = f.read()
    
res = RSA.importKey(tmp)
print(res.d)