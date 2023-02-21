from PIL import Image
img=Image.new('RGB',(250,250),'white')
pixels=img.load()
a=input('Give point A as x,y:')
b=input('Give point B as x,y:')
a=a.split(',')
b=b.split(',')
a=list(map(lambda x: int(x), a))
b=list(map(lambda x: int(x), b))

k=(b[1]-a[1])/(b[0]-a[0])
q=a[1]-k*a[0]

for x in range(a[0],b[0]+1):
    y=int(k*x+q)
    pixels[x,y]=(255,0,0)
    print(x,y)
    while pixels[x-1,y-1] != (255,0,0) and x!=y:
        pixels[x,y-1] = (255,0,0)
        y = y-1
        print(x,y)
        #img.show()
    #img.show()
img.show()