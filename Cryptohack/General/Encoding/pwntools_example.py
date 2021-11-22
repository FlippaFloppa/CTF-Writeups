from pwn import * # pip install pwntools
import json
import codecs
import binascii

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decoder(encoding,challenge_words):
    if encoding == "base64":
            return base64.b64decode(challenge_words).decode('utf-8')
    elif encoding == "hex":
        return binascii.unhexlify(challenge_words).decode('utf-8')
    elif encoding == "rot13":
        return codecs.encode(challenge_words, 'rot_13')
    elif encoding == "bigint":
            return binascii.unhexlify(challenge_words.replace('0x', '')).decode('utf-8')
    elif encoding == "utf-8":
        s = ""
        for c in challenge_words:
            s += chr(c)
        return s
    
while True:
    received = json_recv()
    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)  
    to_send = {"decoded": decoder(received["type"],received["encoded"]) }
    json_send(to_send)


