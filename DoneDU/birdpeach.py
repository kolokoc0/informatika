#after each consonant a random vowel l -> la/le
#after each wovel - a -> aaa
def translate(ret):
    poc = 0
    samo = "aeiouy"
    spol = "qwrtpsdfghjklzxcvbnm"
    vys =""
    while poc < len(ret):
        if ret[poc] in samo or ret[poc] in samo.upper():
            vys += ret[poc]
            poc +=3
        else:
            if ret[poc] in spol or ret[poc] in spol.upper():
                vys += ret[poc]
                poc +=2
            else:
                vys += ret[poc]
                poc +=1
    return vys



print(translate("hieeelalaooo"))
