table = []
start = 65
end = 90
for i in range(65,91):
    array2 = []
    for j in range(start, end+1):
        if j > 90:
            a = j - 26
            array2.append(chr(a))
        else:
            array2.append(chr(j))   
    table.append(array2)
    start += 1
    end += 1

ENCRYPTED = "UFJKXQZQUNB"
KEY = "SOLVECRYPTO"

enc = []
key = []
out = ""
for i in range(len(ENCRYPTED)):
    toNumEnc = ord(ENCRYPTED[i]) - 65
    toKeyEnc = ord(KEY[i]) - 65
    out += table[toKeyEnc][toNumEnc]
    enc.append(toNumEnc)
    key.append(toKeyEnc)

print(enc)
print(key)
print(out)