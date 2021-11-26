encrypt = 'dspttjohuifsvcjdpoabrkttds'

for i in range(27):
    out = ''
    for decrypt in encrypt:
        a = ord(decrypt) - i
        a = chr(a)
        out += a
    print('picoCTF{'+str(out)+'}')
