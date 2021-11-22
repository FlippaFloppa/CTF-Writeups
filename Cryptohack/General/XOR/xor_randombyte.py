import pwn as pwn
from binascii import unhexlify

val = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
b = unhexlify(val)

for i in range(100):
    res=(pwn.xor(b,i))
    if("crypto" in str(res)):
        print(str(res))