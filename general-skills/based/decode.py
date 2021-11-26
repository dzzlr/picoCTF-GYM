a = '01101100 01101001 01111010 01100001 01110010 01100100'
a = a.split()
ascii_str = ''
for bin_val in a:
	integer = int(bin_val, 2)
	ascii_chr = chr(integer)
	ascii_str += ascii_chr
print(ascii_str)

b = '154 141 155 160'
b = b.split()
ascii_str = ''
for oct_char in b:
	ascii_chr = chr(int(oct_char, 8))
	ascii_str += ascii_chr
print(ascii_str)

c = bytearray.fromhex("66616c636f6e").decode()
print(c)