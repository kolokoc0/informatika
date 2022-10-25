# a = input(" Daj slovo: ")
#
# b = len(a)
#
# c = b//2
# f = 0
# for i in range (0,c):
#     b -= 1
#     if a[i]==a[b]:
#         f +=1
#
# if f == c:
#     print (" jeto palindrom")
# else:
#     print (" nie je to palindrom")

# TOTo je ten palindrom hore je  co ja som spravil
# ret = input("Daj slovo: ")
# dc = len(ret)//2
# status = True
# for i in range(dc):
#     if ret[i]!=ret[len(ret)-1-i]:
#         status = False
#         break  #nie je to najlepsie pouzit
#
# print (status)

#rezy
# jozo = "PLC#F"
# fero = jozo[1:3]
# print (fero)
# jana = jozo[::-1]
# print (jana)
# obrati to string takze F#CLP

#lahsi program na palindrom
#
# ret = input("daj slovo: ")
# dc = ret[::-1]
# if ret==dc:
#     print ("palindrom")

#ukaze uhol pod ktorym je slnko ak zacina o 6 a konci o 18 vychod slnka
#ret = input("Zadaj mi retazec (hh:mm): ")
# a,b = ret.split(":")
# a = int(a)
# b = int(b)
# if a<6 or a>18:
#     print ("Tma")
# else:
#     min = ((a-6)*60)+b
#     uhol = (min*180)/720
#     print (uhol)
# Nacitaj cas a vypocitaj uhol medzi rucickami rucickovych hodin

# ret  = input("Zadaj mi retazec (hh:mm): ")
# h,m = ret.split(":")
# h = int(h)
# m = int(m)
# if h>12:
#     h -=12
# alpha = 360/60*m
# beta = (30*h)+(30*m/60)
# uhol = abs(alpha-beta)
# print (uhol)
# Ci sa nejaky string nachadza v inom
text = "Sedi mucha na stene sedi, a spi, sedi a buvinka potvora malinka"
samo = "aeiouy"
schym = input("Zadaj samohlasku ktoru tam kdes: ")
nt="" #nemoze tam byt ani medzera
for i in text:
    if i in samo: #zisti ci to i (prve S) sa nachadza v retazci samo
        nt = nt + schym #spaja retazce
    else:
        nt = nt + i
print (nt)
