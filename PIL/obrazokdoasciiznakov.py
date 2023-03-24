from PIL import Image

#img = Image.open("obrazok.png")
##Obrazok je 750x500
#img = img.resize((100,100))
#
#subor = open("ASCIIznaky.txt","w",encoding="UTF-8")
#
#density = 'Ñ@#W$9876543210?!abc;:+=-,._       '[::-1]
#def mapovanie(a,b,c,d,x):
#    return int((x*(d-c)-(a*d)+(c*b))/(b-a))
#
#pixels = img.load()
#def svetlost(pixel):
#    return ((sum(pixel))/3)
#for y in range(img.size[1]):
#    subor.write('\n')
#    for x in range(img.size[0]):
#        avg = svetlost(pixels[x,y])
#        cislo = mapovanie(0,255,0,len(density),avg)
#        subor.write(str(density[cislo]))
#subor.close()
#img.show()


subor = open("kompresia_obrazka_1.txt","r")
fl = subor.readline().split()
print(fl)
poc = 0

newimg = Image.new("RGB",(int(fl[0]),int(fl[1])),"white")
pixels = newimg.load()
#prechadzam textovy subor
for line in subor:
    for i in range(len(line)-1):
        if line[i] == "1":
            pixels[i,poc] = (255,255,255)
        else:
            pixels[i,poc] = (0,0,0)
    poc+=1
newimg.show()



