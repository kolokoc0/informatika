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
zoz1 = [2,7,10,16,58]
zoz2 = [15,16,18,20]
zoz = [ ]
poc = 0
def merge(zoz1,zoz2):
    for i in zoz2:
        for a in zoz1:
            if i>a and i not in zoz and a not in zoz:
                zoz.append(a)
            else:
                zoz.append(i)
                break
    return zoz
print (merge(zoz1,zoz2))
