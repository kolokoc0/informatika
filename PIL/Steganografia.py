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



