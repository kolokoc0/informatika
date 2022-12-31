meno = input("zadaj nazov suboru")
def otvor(meno ='text.txt'):
    return open('data/'+meno, 'r', encoding ='UTF-8')
fr = otvor(meno)
def spracuj_subor(fr):
    poc = 0
    riadky = fr.readlines()
    temp = riadky[1].strip()
    slova = temp.split(' ')
    print("'"+riadky[1].strip()+"'")
    print(slova[0])
    #print(temp.count(" "))
    for i in temp:
        if i ==" ":
            poc +=1
    print(poc)
spracuj_subor(fr)
fr.seek(0)
# shift + f6 premeni vsetky vyskyty premeny napr oznacim nula na jozo
def sirka(fr):
    nula = 0
    for i in fr:
        if len(i)>nula:
            nula = len(i)
    return (nula)
print(sirka(fr))
