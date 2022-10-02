a= int(input("Zadaj Cislo"))
sum = 0
pocitadlo = 0
priemer = 0
while (a!=0):
    print (a)
    sum += a
    a= int(input("Zadaj dalsie Cislo"))
    pocitadlo += 1
    priemer = float(sum/pocitadlo)

print (priemer)