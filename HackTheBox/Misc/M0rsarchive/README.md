## WriteUp for the challenge [M0rsarchive](https://app.hackthebox.com/challenges/m0rsarchive)

After the extraction of the zip we see a file, pwd.jpg that has inside the password in morse code for the next zip.
This seems like a matrioska challenge. All we need is to find a way to quickly decode morse code.

There is a [OCR morse code tool](https://github.com/eauxfolles/morse-ocr) we can use to decode all the passwords.

Then the game is to automatize all the process. We can do it with a simple bash script.


````bash
#!/bin/bash

for i in {999..0}; do
res=$(./mocr.py pwd.png | tr -d '\n')
unzip -o -j -P $res "flag_$i.zip"
done
````

At the end we got a file with the flag inside.
