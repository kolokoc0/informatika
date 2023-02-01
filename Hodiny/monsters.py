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
    #7 percentna mutacia
    #mutacia ak nastane ta 7% sanca tak vygenerujem na to miesto random cislo od 0-9
    mutationindex = random.randrange(0,101)
    if mutationindex>93:



