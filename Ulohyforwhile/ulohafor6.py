a = int(input("Zaciatok uzavreteho intervalu"))
b = int(input("Koniec uzavreteho intervalu"))
pocitadlo = 0
for i in range (a,b+1):
    if i !=0:
        if i%8 ==0:
            pocitadlo += 1
        
        
print (pocitadlo)