
import random
#zoz = []
#for i in range(10):
#    zoz.append(random.randrange(0,100))
#print (zoz)
##vybrat nahodny prvok
#index = random.randrange(0,10)
#print(zoz[index])
#
##vdaka random
#print(random.choice(zoz))
##Triedenie zoznamu
#nov_zoz = sorted(zoz)#Vytvori novy zoznam ktory je potriedeny
#print (nov_zoz)
#zoz.sort()#Utriedi samotny zoznam
#print(zoz)
zoz = []
for i in range(10):
    zoz.append(random.randrange(0,100))
print(zoz)
#Vyberove triedenie
def findmaximum(index:int)->int:
    max_value = zoz[index]
    max_index = index
    for i in range(index,len(zoz)):
        if zoz[i] > max_value:
            max_value = zoz[i]
            max_index = i
    return (max_index)
print(findmaximum(0))
#zober to co ti vyjde a vymen s nulou
for i in range(len(zoz)):
    max_index = findmaximum(i)
    zoz[i], zoz[max_index] = zoz[max_index], zoz[i]
print(zoz)
#Bublinkove triedenie - naprogramuj doma for i in range(0,len(text), -1 (step)):
