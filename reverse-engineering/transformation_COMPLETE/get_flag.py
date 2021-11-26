#!/usr/bin/python3
file = open('enc', 'r')
a = file.read()

hex_string = ''
for i in range(len(a)):
    hex_string += hex(ord(a[i])).lstrip('0x')

bytes_obj = bytes.fromhex(hex_string)
flag = bytes_obj.decode("ASCII")

print(flag)
