a = input(" Daj slovo: ")

b = len(a)
d = len(a)

c = b//2
f = 0
for i in range (0,c):
    b -= 1
    if a[i]==a[b]:
        f +=1

if f == c:
    print (" jeto palindrom")
else:
    print (" nie je to palindrom")
    
