from PIL import Image, ImageOps
#img = Image.open("Obrazok.png")

#img = img.resize((700,500))
#img2 = Image.new("RGB",img.size,"white")
#pixels_in = img.load()
#pixels_out = img2.load()

# Obratenie cez os y

#for x in range(1,img.size[0]):
#     for y in range(img.size[1]):
#         pixels_out[img.size[0]-x,y] = pixels_in[x,y]
#img.show()
#img2.show()

#Zmensenie obrazka

#for x in range(0,img.size[0],2):
#    for y in range(0,img.size[1],2):
#        pixels_out[x//2,y//2] = pixels_in[x,y]
#img2.show()

#zvacsenie obrazka

# img2 = Image.new("RGB",(img.size[0]*2,img.size[1]*2))
# pixels_in = img.load()
# pixels_out = img2.load()
# for x in range(0,img.size[0]):
#     for y in range(0,img.size[1]):
#         pixels_out[2*x,2*y] = pixels_in[x,y]
#         pixels_out[(2*x)+1,2*y] = pixels_in[x,y]
#         pixels_out[2*x,(2*y)+1] = pixels_in[x,y]
#         pixels_out[(2*x)+1,(2*y)+1] = pixels_in[x,y]
# img2.show()


#for x in range(img.size[0]):
#    for y in range(img.size[1]):
#        pixels_out[x,y] = pixels_in[-1-x,-1-y]
#img2.show()
img = Image.open("Obrazok.png")

img = img.resize((700,500))
img1 = ImageOps.grayscale(img)

fw = open("Vysledok.txt", "w", encoding="UTF-8")
fw.write(str(img1.size[0])+" "+ str(img1.size[1])+'\n')
pixels = img1.load()
for y in range(img1.size[1]):
    for x in range(img1.size[0]):
        #sefovacka dorobit zapis do suboru ale ak mas dlzku jedna tak pridas 0
        a = hex(pixels[x,y])[2::]
        if len(a) == 1:
            a = "0"+a
        fw.write(a)
    fw.write("\n")
fw.close()



