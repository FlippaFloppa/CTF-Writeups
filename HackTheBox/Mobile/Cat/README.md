## WriteUp for the challenge [Cat](https://app.hackthebox.com/challenges/115)


Initially we have a file named "cat.ab". With the file command we can see what it really is:

`file cat.ab`

The result is that is an **"Android Backup, version 5, Compressed, Not-Encrypted"** file. 
This means that we have to extract it into the effective Android Backup file. To do that we can simply use [android-backup-extractor](https://github.com/nelenkov/android-backup-extractor) to unpack the zipped file.

`java -jar abe.jar unpack cat.ab res.tar`

And then untar the file with:

`tar -xf res.tar`

This will generate a lot of folders. If we search for big file size with `du -hs *` we will notice that inside **/shared/0/Pictures** there are a lot of photos.

Search through cat photos and you will se the flag!
