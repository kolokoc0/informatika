#import random as rn
#zoz = [ ]
#for i in range (10):
#   zoz.append(rn.randrange(0,21))
#print (zoz)
#print(*zoz)

#import random
#zoz = [ ]
#for i in range(10):
#    zoz. append(random.randrange(0,21))
#print(zoz)
#maximum = zoz[0]
#poz = 0
#for i in range(1, (len(zoz))):
#    if (zoz[i])>maximum:
#        maximum = zoz[i]
#        poz = i
#print ("najvacsi prvok je", maximum, "na pozici", poz)
#pocpar = 0
#pocparna = 0
#pocnepar= 0
#pocneparna = 0
#for i in range(0,len(zoz)):
#    if zoz[i]%2 == 0:
#        pocpar +=1
#    else:
#        pocnepar +=1
#    if zoz[i]%2 ==0 and i%2==0:
#        pocparna += 1
#    else:
#        if zoz[i]%2!= 0 and i%2!= 0:
#            pocneparna += 1
#print("Parne", pocpar, "neparne", pocnepar)
#print(pocparna, pocneparna)
zoz2 = [10,16,58]
zoz1 = [20,98]
def merge(zoz1,zoz2):
    dlz = len(zoz1)
    dlz2 = len(zoz2)
    poc = 0
    poc2 = 0
    zoz = [ ]
    while poc<dlz and poc2<dlz2:
        if zoz1[poc]<zoz2[poc2]:
            zoz.append(zoz1[poc])
            poc +=1
        else:
            zoz.append(zoz2[poc2])
            poc2 += 1
    zoz = zoz +zoz1[poc:] + zoz2[poc2:]
  
    return zoz
print (merge(zoz1,zoz2))
