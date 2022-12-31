fr = open('data/zvieratka.txt',"r", encoding ="UTF-8")
def zviera(subor):
    zoo = {}
    zoo3 = {}
    for line in subor:
        temp = line.strip().split(" ") #keby bol len split tak ti to vrati zoznam, strip z toho spravi string
        zoo[temp[0]] = int(temp[1]) # v podstate do zoo prida temp[0] - kluc co je meno zvierata priradim temp[1]
    zoo2 = sorted(zoo)
    for i in zoo2:
        zoo3[i] = zoo[i] # zoo3[i] ti najde zviera = zoo[i] hodnotu da zvieratu z povodneho
    priemer = 0
    for i in zoo3:
        priemer += zoo3[i]
    priemer = priemer/len(zoo3)
    print(priemer)
    return zoo3
print(zviera(fr))
fr.seek(0)
def najtazsi(subor):
    zoo = {}
    for line in subor:
        temp = line.strip().split(" ")
        zoo[temp[0]] = int(temp[1])
    naj = list(zoo.keys())[0] # len zoo.keys vracia objekt nemozem vyberat z neho musim spravit zoznam
    for kluc in zoo.keys():
        if zoo[kluc]> zoo[naj]:
            naj = kluc
    return(naj,zoo[naj])
print(najtazsi(fr))
fr.seek(0)
zoo = {}
for line in fr:
    temp = line.strip().split(" ")
    zoo[temp[0]] = int(temp[1])
def tazsie_ako(vz):
    newzoo = {}
    for zviera in zoo:
        if zoo[zviera]> zoo[vz]:
            newzoo[zviera] = zoo[zviera]
    return newzoo
print(tazsie_ako("diviak"))



