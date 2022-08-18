## WriteUp for the challenge [Don't Overreact](https://app.hackthebox.com/challenges/dont-overreact)

We have an APK, then we just have to extract it with:

`unzip app-release.apk`

This gives us all the directories and files of the application. Now we search for hints with 

`find .  -type f -exec cat {} + | grep -a "htb"` But we find only a logo.

Let's try with

`find .  -type f -exec cat {} + | grep -a "hackthebox"`

Now we see inside the file **assets/index.android.bundle** this debug information 


`__d(function(g,r,i,a,m,e,d){Object.defineProperty(e,"__esModule",{value:!0}),e.myConfig=void 0;var t={importantData:"baNaNa".toLowerCase(),apiUrl:'https://www.hackthebox.eu/',debug:'SFRCezIzbTQxbl9jNDFtXzRuZF9kMG43XzB2MzIyMzRjN30='};e.myConfig=t},400,[]);`

We read **SFRCezIzbTQxbl9jNDFtXzRuZF9kMG43XzB2MzIyMzRjN30=**

This is clearly a base64 encoded text. Let's decode it with Cyberchef and we have the flag!
