#vytvorte funkciu vypis ktora ma jeden vstupny parameter - string a funkcia vypise pre kazdy znak tohto retazca 4 udaje:
# a to jeho poradove cislo, jeho ascii hodnotu, samotny znak, a znak ktory nasleduje za nim

def vypis(retazec:str):
    n = len(retazec)
    poc = -1
    for i in retazec:
        poc +=1
        a = ord (i)
        b = (ord (i))+1
        b = chr(b)
        print ("Zmak:",i,"Poradove cislo:",poc,"Ascii hodnota:",a,"Znak ktory nasledujuje:",b)
vypis(input("Napis nieco: "))
