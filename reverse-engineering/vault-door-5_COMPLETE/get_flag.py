#!/usr/bin/python3
import base64
from urllib.parse import unquote

flag = 'JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2'

base64_out = base64.b64decode(flag).decode('utf-8')
url_out = unquote(base64_out)

print("picoCTF{{{}}}".format(''.join(url_out)))
