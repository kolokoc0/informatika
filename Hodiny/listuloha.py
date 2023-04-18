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