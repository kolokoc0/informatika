def obdlznik(sirka:int, znak:str):
    for i in range (0,3):
        vys =""
        if i!=1:
            for a in range(0,sirka):
                vys += znak
        else:
            for a in range(0, sirka):
                if a!=0 and a!=sirka-1:
                    vys += " "
                else:
                    vys += znak
        print(vys, end="\n")


obdlznik(int(input("Zadajcislo")),input("Daj znak"))
