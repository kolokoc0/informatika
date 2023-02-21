from PIL import Image
sprava = "Ahoj svet#"
dlzka = 8
img = Image.open("Obrazok.png")
img = img.resize((700,500))
pixels = img.load()
def priprav(sprava:str) ->list:
    res = []
    for pismenko in sprava:
        cislo = (bin(ord(pismenko)))
        cislo = str(cislo[2::])
        #while len(cislo)<dlzka:
            #cislo = "0" + cislo
        cislo = (dlzka-len(cislo))*"0" + cislo
        for j in cislo:
            res.append(int(j))
    return (res)
print(priprav(sprava))
def drticka(sprava):
    spravavcisla = priprav(sprava)
    for i in range(len(spravavcisla)):
        sirka = img.size[0]
        # vyska = img.size[1]
        x = i% sirka
        y = i// sirka
        modra = pixels[x,y][2]
        newblue = int((bin(modra)[2:-1:]) + str(spravavcisla[i]),2)
        newcolor = (pixels[x,y][0],pixels[x,y][1],newblue)
        pixels[x,y] = newcolor
drticka(sprava)
s = ord('A')
s = bin(s)
print(bin(pixels[0,0][2]))
def odrticka(img):
    binary = ""
    string = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if "#" in string:
                return string
            last_modra = str(bin(pixels[x,y][2]))[-1]
            binary += last_modra
            space = (bin(ord(" "))[2::])
            hash = (bin(ord("#"))[2::])
            if len(binary) == 8 or binary[2::] == space or binary[2::] == hash:
                string += chr(int((binary),2))
                binary = ""
print(odrticka(img)) 

