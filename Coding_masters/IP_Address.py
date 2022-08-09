a = "192.168.35.19"
b = "fe80:0000:9c35:ad16:e546:a983:bbcf" 

if(b.find(':')!= -1):
    print("IPv6")
elif(b.find(".")!= -1):
    print("IPv4")