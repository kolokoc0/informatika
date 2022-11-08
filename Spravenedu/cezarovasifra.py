#v zosite 2.11.
def cezar_encoder(text,posun):
    ret = ""
    for i in text:
        i = chr((ord(i)-97 + posun)%26 + 97)
        ret += i
    return ret
print(cezar_encoder(input("Kodovane slovo: "),int(input("Posun: "))))
