import base64
import hashlib

data = 

"""
Z85 0...9, a...z, A...Z, ., -, :, +, =, ^, !, /, *, ?, &, <, >, (, ), [, ], {, }, @, %, $, #. 
=*&<>| not supported by oracle
@%+\/'!#$^?:,(){}[]~`-_. Supported by Oracle
>>> data = 'The quick brown fox jumped over the lazy dog.'
>>> m = hashlib.md5(data.encode('ascii'))
>>> base64.b16encode(m.digest())
b'5C6FFBDD40D9556B73A21E63C3E0E904'
>>> base64.b85encode(m.digest())
b'TyOi`K-pDmbD|z&!{F%z'

# generate a password with length "passlen" with no duplicate characters in the

import random

string_set = "0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ~!@#$%^&*(){}?-_=+"
passlen = 8
p =  "".join(random.sample(string_set,passlen ))
print p

'''

0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_+-=/\|()[]{},.?:;`~"'
0123456789aåäbcdefghijklmnoöpqrstuüvwxyzAÅÄBCDEFGHIJKLMNOÖPQRSTUÜVWXYZ~!@#$%^&*/\"'`()[]{}?-_=+


'''

import base64
# Creating a string
s = "Hello World!"
# Encoding the string into bytes
b = s.encode("UTF-8")
# Base85 Encode the bytes
e = base64.b85encode(b)
# Decoding the Base85 bytes to string
s1 = e.decode("UTF-8")
# Printing Base85 encoded string
print("Base85 Encoded:", s1)
# Encoding the Base85 encoded string into bytes
b1 = s1.encode("UTF-8")
# Decoding the Base85 bytes
d = base64.b85decode(b1)
# Decoding the bytes to string
s2 = d.decode("UTF-8")
print(s2)

"""