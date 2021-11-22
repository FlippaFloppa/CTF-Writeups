import pwn as pwn
from binascii import unhexlify

val = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
key = "crypto{"
b = unhexlify(val)
keylen=len(key)
print(keylen)
#xor between the first 7 letters of the key [0-6]
tmp = pwn.xor(key.encode(),b[:keylen])
tmp_key=(tmp+"y".encode())
readable=tmp_key.decode("utf-8")
result=""

#for every 8 keys i add myXORkey
for i in range (int(len(val)/2)):
    result+=readable[int(i%(keylen+1))]

print("KEY ---> "+result)
print("FLAG ---> "+pwn.xor((result.encode()),b).decode("utf-8"))
