# def fak(cislo):
#     vys = 1
#     for i in range(2,cislo+1):
#         vys*=i
#     return vys
#
# def kon(n:int,k:int):
#     return (fak(n)//(fak(n-k)*fak(k)))
#
#
# def pasc(riadok:int):
#     for i in range (riadok+1):
#         for a in range (0,i+1):
#             print (kon(i,a), end =" ")
#
#         print (" ")
#
# pasc(5)

def colatz(cislo:int):
    while cislo !=1:
        if cislo %3 ==0 or cislo%3 !=0 and cislo %2 !=0:
            cislo *=3
            cislo +=1
            print (cislo, end =" ")
        else:
            if cislo %2 ==0:
                cislo /=2
            print (cislo, end =" ")

colatz (13)

