import base64

def start():
selekto=input("Enkodim apo Dekodim? ")
if selekto=="Enkodim":

    mssg=input("Enter your message:")
    mssgencoded = mssg.encode("UTF-8")
    mssgtob64 = base64.b32encode(mssgencoded)
    mssgdecoded = mssgtob64.decode("UTF-8")
    print("Base32 Encoded:", mssgdecoded)
    showmsg=input("Do you want to return to encoding/decoding (Yes/No): ")
        if showmsg=="Yes":
            start()
        else:
            print("Process has terminated")
    
elif selekto=="Dekodim":
    mssg=input("Enter your message:")
    mssgencoded2 = mssg.encode("UTF-8")
    mssgdecoded2 = base64.b32decode(mssgencoded2)
    finalmssg = mssgdecoded2.decode("UTF-8")
    print(finalmssg)
    showmsg=input("Do you want to return to encoding/decoding (Yes/No): ")
        if showmsg=="Yes":
            start()
        else:
            print("Process has terminated")
else:
    print("Duhet te shkruani Enkodim ose Dekodim")
    
    
start()
