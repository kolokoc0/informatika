
def troj (strana:int):
    for i in range (1,strana+strana,2):
        vys = ""
        d = ((2*strana-i)//2)
        vys += d*" "
        for a in range (i):
            vys += "*"
        vys += d*" "
        print (vys)
    
troj (int(input("Zadajte dlzku strany: ")))