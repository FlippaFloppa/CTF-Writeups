import pwn as pwn
from binascii import unhexlify

#transform in bytes
KEY1=unhexlify("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY4=unhexlify("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
KEY2KEY1=unhexlify("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2KEY3=unhexlify("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

#xor associative
KEY2=(pwn.xor(KEY1,KEY2KEY1))
KEY3=(pwn.xor(KEY2,KEY2KEY3))
FLAG=(pwn.xor(KEY4,KEY3,KEY2,KEY1))

print("KEY1 ----> "+str(KEY1))
print("KEY2 ----> "+str(KEY2))
print("KEY3 ----> "+str(KEY3))
print("KEY4 ----> "+str(KEY4))
print("FLAG ----> "+str(FLAG))
