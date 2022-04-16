import base64
s="A simple example of encoding and decoding in python!!"
print("Message:",s)
b=s.encode("UTF-8")
e=base64.b32encode(b)
s1=e.decode("UTF-8")
print("Base32 Encoded:",s1)
b1=s1.encode("UTF-8")
d=base64.b32decode(b1)
s2=d.decode("UTF-8")
print("Base32 Decoded:",s2)
