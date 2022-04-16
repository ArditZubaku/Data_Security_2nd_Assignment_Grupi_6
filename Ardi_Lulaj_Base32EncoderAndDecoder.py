import base64

var =int(input("To Encode press 1 , To Decode press 2  :"))


if var == 1:
    print("You have chosen to encode in Base32")
    s=input("Write the String you want to encode : ")
    b = s.encode("UTF-8")
    e = base64.b32encode(b)
    s1 = e.decode("UTF-8")
    print("Base32 Encoded:", s1)
elif var == 2:
    print("You have chosen to decode from Base32")
    b1 = input("Enter Coded String to Decode: ")
    d = base64.b32decode(b1)
    s2 = d.decode("UTF-8")
    print(s2)
else:
    print("Input is not a valid option, please choose 1 or 2")