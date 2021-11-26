# hex_string = '51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959'
# bytes_obj = bytes.fromhex(hex_string)
# flag = bytes_obj.decode("ASCII")

# print(flag)

p = 's'
k = 64
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), p, k))
print(result)