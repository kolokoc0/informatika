a = int(input("Cislo: "))

b= a%100
c= b//10
d= b%10
e= d+c

if e%2==0:
    print ("Sucet poslednych dvoch cifier je parny")
else:
    print ("Sucet poslednych dvoch cifier je neparny")
