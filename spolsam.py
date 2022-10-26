#striedanie spol a sam v 10 znakoch
import random
def alter(dlzka=5):
    samo = "aeiouy"
    spol = "qwrtpsdfghjklzxcvbnm"
    vys =""
    for i in range(dlzka):
        # vys += random.choice(spol)
        index = random.randrange(0,len(spol))
        vys += spol[index]
        # vys += random.choice(samo)
        index2 = random.randrange(0,len(samo))
        vys += samo[index2]
    return vys
print(alter())

