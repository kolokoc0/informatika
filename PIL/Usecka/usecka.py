from PIL import Image
img=Image.new('RGB',(250,250),'white')
pixels=img.load()
a=input('Give point A as x,y:')
b=input('Give point B as x,y:')
a=a.split(',')
b=b.split(',')
a=list(map(lambda x: int(x), a))
b=list(map(lambda x: int(x), b))
if a[0]>b[0] and a[1] > b[1] or a[0]>b[0] and a[1]<b[1]:
    a,b = b,a

k=(b[1]-a[1])/(b[0]-a[0])
q=a[1]-k*a[0]
temp = int(k*a[0]+q)
for x in range(a[0],b[0]+1):
    y=int(k*x+q)
    pixels[x,y]=(255,0,0)
    print(x,y)
    vektor = (b[0]-a[0],b[1]-a[1])
    vektor = (vektor[1],vektor[0]*(-1))
    if vektor[0]<0 and vektor[1]<0:
        vektor = (vektor[0]*(-1),vektor[1]*(-1))
    c = float((-1)*(vektor[0]*a[0] + vektor[1]*a[1]))
    if (abs(y -temp)) >1:
        for i in range(1,abs(y-temp)):
            if y<temp:
                i = i*(-1)
            new_x = round((vektor[1]*(temp+i)*(-1)+c*(-1))/(vektor[0]))
            print(new_x,temp+i)
            pixels[new_x,temp+i] = (255,0,0) 
    temp = y
img.show()