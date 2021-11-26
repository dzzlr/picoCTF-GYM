import base64

flag = open("hidden", "r")
clean_flag = str(flag.read().replace(" ",""))

print(clean_flag)
flag_decode = base64.b64decode(clean_flag)
print(flag_decode)