a = int(input("Napis konecnu hranicu uzatvoreneho intervalu"))
pocitadlo = 0
for i in range (1, a+1):
    if i%7 ==0 and i%4 ==0:
        pocitadlo +=1

print (pocitadlo)