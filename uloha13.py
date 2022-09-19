import math as math


a = int(input("Cislo: "))
b = int(input("Cislo: "))
c = int(input("Cislo: "))




if a+b>c and a+c>b and c+b>a:
    beta=((b**2-(a**2+c**2))/(-(2*a*c)))
    beta=math.acos(beta)
    beta=math.degrees(beta)
    print (beta)



    alpha=((a**2-b**2-c**2)/(-(2*b*c)))
    alpha=math.acos(alpha)
    alpha=math.degrees(alpha)
    print (alpha)

    gamma=((c**2-a**2-b**2)/(-(2*a*b)))
    gamma=math.acos(gamma)
    gamma=math.degrees(gamma)
    print (gamma)
else:
    "Takyto trojuholnik neexistuje"


if a+b>c and a+c>b and c+b>a:
    if beta==90 or gamma==90 or alpha==90:
        print("Pravouhly")
    else:
        if beta>90 or alpha>90 or gamma>90:
                print ("tupy")
        else:
            if beta<90 and alpha<90 or beta<90 and gamma<90 or alpha<90 and gamma<90: 
                print ("Ostry")
else:
    print ("Takyto trojuhlnik neexistuje")
             
if a+b>c and a+c>b and c+b>a:
    if gamma==beta==alpha:
        print ("Rovnostranny")
    else:
        if gamma==beta or gamma==alpha or beta==alpha:
            print ("Rovnoramenny")
        else:
            print ("Rozno stranny")



