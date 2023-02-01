#napiste program ktory vygeneruje obrazok 100x100 pixelov a na miesta kde sucet suradnic je parny bude cierny pixel a kde sucet neparny polozim zlty
from PIL import Image
img = Image.new("RGB", (100,100))
pixels = img.load()

for y in range(img.size[0]):
    for x in range(img.size[1]):
        if (x+y)%2==0:
            pixels[x,y] = (0,0,0)
        else:
            pixels[x,y] = (250,250,0)
img.show()
