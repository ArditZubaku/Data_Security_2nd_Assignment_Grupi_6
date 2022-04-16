import base64

selekto=input("Enkodim apo Dekodim? ")
if selekto=="Enkodim":

    mssg=input("Enter your message:")
    mssgencoded = mssg.encode("UTF-8")
    mssgtob64 = base64.b32encode(mssgencoded)
    mssgdecoded = mssgtob64.decode("UTF-8")
    print("Base32 Encoded:", mssgdecoded)
