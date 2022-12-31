zoz = [2,5,7,12,1,6]
def bubble(zoz):
    for i in range(len(zoz)):
        for a in range(len(zoz)-1):
            if zoz[a]>zoz[a+1]:
                zoz[a], zoz[a+1] = zoz[a+1], zoz[a]
    return zoz
print(bubble(zoz))
