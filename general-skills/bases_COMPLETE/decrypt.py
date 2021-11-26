import base64

a = 'bDNhcm5fdGgzX3IwcDM1'
out = base64.b64decode(a).decode("utf-8")
print("picoCTF{"+out+"}")
