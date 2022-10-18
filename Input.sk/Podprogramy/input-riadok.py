def riadok(n, text):
    vys = ""
    dlzte = len(text)
    if text!="":
        n -= (dlzte+2)
        vys += (((n)//2)*"*")
        vys += " "+ text + " "
        vys += (((n)//2)*"*")
    else:
        vys += n*"*"
    print (vys)
riadok (int(input("Vloz pocet: ")),input("Vloz text: "))