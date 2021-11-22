import Crypto.Util.number as crypto

#message(string) -> bytes -> hex(concat) -> base16 / base10
val = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

res = crypto.long_to_bytes(val)
undo_res = crypto.bytes_to_long(res)

print(str(res)+" <--- ("+str(undo_res)+")")
