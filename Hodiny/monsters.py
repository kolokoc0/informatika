import random
monsters =[]
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
            babo.append(random.randrange(1,10))
        else:
            chance = random.randrange(1,101)
            if chance>50:
                babo.append(monster2[i])
            else:
                babo.append(monster1[i])
    return babo



