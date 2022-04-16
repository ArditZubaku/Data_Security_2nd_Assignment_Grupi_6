import base64

selekto=input("Enkodim apo Dekodim? ")
if selekto=="Enkodim":

    mssg=input("Enter your message:")
    mssgencoded = mssg.encode("UTF-8")
    mssgtob64 = base64.b32encode(mssgencoded)
    mssgdecoded = mssgtob64.decode("UTF-8")
    print("Base32 Encoded:", mssgdecoded)
    
elif selekto=="Dekodim":
    mssg=input("Enter your message:")
    mssgencoded2 = mssg.encode("UTF-8")
    mssgdecoded2 = base64.b32decode(mssgencoded2)
    finalmssg = mssgdecoded2.decode("UTF-8")
    print(finalmssg)
else:
    print("Duhet te shkruani Enkodim ose Dekodim")
