CHALLENGE 01

Your files have been compromised, get them back.

Hint: Find a way to make sense of it.

↗ OPEN CHALLENGE
this downloads 2 a zip with two files:
```
-rw-r-----@      256 flag
-rwxr-x---@  3294254 wannacry
```

We used cutter to inspect the executable and were really concerned about actually running it. We spent quite some time trying to see how we can reverse-engineer it, realising we have no clue what we are looking at or how to use it.


We got a computer with a new ubuntu install and tried it out and got `help`.

We need to provide `-encrypted_file` and `-key_file`
```
Usage of ./wannacry: 
    -encrypted_file string 
        File name to decrypt. 
    -key_file string 
        File name of the private key. 
```

We managed to generate a key that passed validation but the output did not make sense.
```
ssh-keygen -t rsa -f key.pem -m pem
openssl rsa -in key.pem -out rsakey.pem
```

We used [strings](https://manpages.ubuntu.com/manpages/bionic/man1/alpha-linux-gnu-strings.1.html) to see if there is anything we can scrape. We checked flag and http and found a link.
```
strings wannacry | grep flag
strings wannacry | grep http
```

At the link https://wannacry-keys-dot-gweb-h4ck1ng-g00gl3.uc.r.appspot.com/ we found 200 keys
```
wget -r --no-parent https://wannacry-keys-dot-gweb-h4ck1ng-g00gl3.uc.r.appspot.com/
```

We ran all keys over the flag and then saw which was listed as and `ASCII text`
```
wannacry-keys-dot-gweb-h4ck1ng-g00gl3.uc.r.appspot.com/2baf7e81-af62-42f7-87d9-bd2b29ff1bc5.pem.decr: ASCII text
```
```
find wannacry-keys-dot-gweb-h4ck1ng-g00gl3.uc.r.appspot.com/ -name "*.pem" > paths.txt
for i in $(<paths.txt);do ./wannacry -encrypted_file flag -key_file $i > $i.decr; done
find wannacry-keys-dot-gweb-h4ck1ng-g00gl3.uc.r.appspot.com/ -name "*.decr"  -exec file  {} \;
```

Fin.
