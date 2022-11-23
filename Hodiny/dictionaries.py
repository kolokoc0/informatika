# pd = {}
# fz = {"a":0, "b":5, "auto":418, 418.5:487, "c":[4,8,7]}
# print(fz["c"][-1])# prve zobere c, to druhe poslednu hodnotu
#
# for key in fz:
#     print(key)
#     print(fz[key])
# print(fz)
# print(*fz) vrati len keys

# Z retazca vypis kolko krat sa tam nachadzaju male pismenka z abecedy
# from string import ascii_lowercase
# vstup = input("Zadaj mi retazec")
# poc = {}
# for i in vstup:
    # if i in ascii_lowercase:
        # poc[i] = poc.get(i,0)+1 #poc[i] - hodnota pri i takze i: normalne je tam nula ale ono to spravi ze poc.get(i,0) +1 - zobere hodnotu a ak nema ziadnu da nulu nakoniec +1
# print(poc)




#Funkcia ktora vypise prve 3 najvacsie polozoky
slov = {"item1":45, "item2": 35, "item3": 41.30, "item4": 55,"item5": 24}
#Zodriedit a vypisat prve 3
#1 bez sorted -> sam ho triedim
#2 najdem max a odstranim ho

#Hladam max prvok v slovniku
for i in range(3):                                            #mojmax = slov["item1"] ak to tam necham tak sa moze stat ze ho popnem a bude error
    indexmax = list(slov.keys())[0]
    mojmax = slov[indexmax]                     #indexmax = "item1"
    for prvok in slov:
        if slov[prvok]>mojmax:
            mojmax = slov[prvok]
            indexmax = prvok
    a = slov.pop(indexmax)

    print(a)

