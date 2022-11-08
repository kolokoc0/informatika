a = int(input("Napis konecnu hranicu uzavreteho intervalu"))
pocitadlo = 0
for i in range (1, a+1):
    if i%2 ==0:
        pocitadlo +=1

print (pocitadlo)