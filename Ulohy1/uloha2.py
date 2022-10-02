a = int(input("Najmensia hranica Intervalu a: "))
b = int(input("Najvacsia hranica Intervalu b: "))
c = int(input("Patrí do uzavretého intervalu číslo: "))
if a<b:
    if c<b and c>a or c==b or c==a:
        print (" Číslo "+str(c)+" Patrí do intervalu")
    else:
            print (" Číslo "+str(c)+" Nepatrí do intervalu")
else:
    if c>b and c<a or c==b or c==a:
        print (" Číslo "+str(c)+" Patrí do intervalu")
    else:
        print (" Číslo "+str(c)+" Nepatrí do intervalu")