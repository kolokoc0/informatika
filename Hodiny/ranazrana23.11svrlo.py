#Dany je zoznam ktory je naplneny stringami 10 miest, vytvorte novy zoznam, ktory bude obsahovat pocty
#Samohlasok v jednotlivych stringoch
zoznam = ["jano", "jozo","dano", "mato", "starec", "aeiou","Adriana","Jozefko", "krk","spanok"]
#def samoh(zoz):
#    zoznam2=[]
#    samo = "aeiouy"
#    poc =0
#    for i in zoz:
#        for a in i:
#            if a in samo:
#                poc +=1
#        zoznam2.append(poc)
#        poc = 0
#    return zoznam2
#
#print(samoh(zoznam))
def samoh (zoz):
    poc = 0
    samo = "aeiouy"
    zoznam2 = []
    for index,hodnota in enumerate(zoz):
        for a in hodnota:
            if a in samo:
                poc+=1
        vys = hodnota, poc
        zoznam2.append(vys)
        poc = 0
    return zoznam2
print(samoh(zoznam))
