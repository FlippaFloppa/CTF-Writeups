#hardcoded values came from https://ctflearn.com/challenge/454

import pwn as pwn
from binascii import unhexlify
import sys

try:
    
    val = sys.argv[1]
    key = sys.argv[2]

except:
    
    print("No args found, using hardcoded values")
    val = "BUGMd`sozc0o`sx^0r^`vdr1ld|"
    key = "CTFL"

b = val.encode()
keylen=len(key)

#xor tra le prime n lettere della flag e della chiave
tmp = pwn.xor(key.encode(),b[:keylen])
readable=tmp.decode("utf-8")
result=""

#per ogni n lettere aggiungo a result key
for i in range (int(len(val))):
    result+=readable[int(i%(keylen))]

print("FLAG ---> "+pwn.xor((result.encode()),b).decode("utf-8"))

