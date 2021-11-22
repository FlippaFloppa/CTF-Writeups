import pwn as pwn

def sove_xor(val,number):
    for i in val:
        res.append(chr(int(ord(i))^number))
    print("".join(res))

#xor with n
val = "label"
number = 13
res = [ ]

#my_function
sove_xor(val,number)

#pwntools
print(pwn.xor(val,13))