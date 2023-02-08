import random
monsters =[]
cage = []
def create_monster()->list:
    temp = []
    for i in range(5):
        a = random.randrange(0,10)
        temp.append(a)
    return temp
def iq_test(monster)->int:
    return monster.count(1)
def sex(monster1,monster2):
    babo = []
    #7 percentna mutacia
    #mutacia ak nastane ta 7% sanca tak vygenerujem na to miesto random cislo od 0-9
    for i in range(len(monster1)):
        mutationindex = random.randrange(1,101)
        if mutationindex>93:
            babo.append(random.randrange(0,10))
        else:
            chance = random.randrange(1,101)
            if chance>50:
                babo.append(monster2[i])
            else:
                babo.append(monster1[i])
    return babo

for i in range(10):
    cage.append(create_monster())
print(cage)
def sorting(cage):
    for a in range(len(cage)):
        for i in range(len(cage)-1):
            if iq_test(cage[i])<iq_test(cage[i+1]):
                cage[i],cage[i+1] = cage[i+1], cage[i]
    return cage
def genocida(cage):
    cage = cage[0:len(cage)//2:]
    return cage
for i in range(100):
    cage = sorting(cage)
    cage = genocida(cage)
    monster1 = 0
    monster2 = 0
    for i in range(5):
        while monster1==monster2:
            monster1 = random.randrange(0,5)
            monster2 = random.randrange(0,5)
        cage.append(sex(cage[monster1],cage[monster2]))
print(cage)


