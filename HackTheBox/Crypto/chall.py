import string

# def encryption(msg):
#     ct = []
#     for char in msg:
#         print("Char: ", char)
#         ct.append((123 * char + 18) % 256)
#     return bytes(ct)

def decryption(msg):
        for i in range(0,256):
            pt = []
            res = []
            for char in msg:
                pt.append(((char - 18) * i)% 256)
            for char in pt:
                res.append(chr(char))
            print("".join(res))


# ct = encryption(MSG)
# f = open('./msg.enc','w')
# f.write(ct.hex())

hex_string = '6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'
a = bytearray.fromhex(hex_string)
b = list(a)
dec = decryption(b)
# f.close()


