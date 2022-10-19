#def riadok(n, text):
#      vys = ""
#      dlzte = len(text)
#      if text!="":
#          n -= (dlzte+2)
#          if n%2==0:
#              vys += ((((n)//2)*"*")
#              vys += " "+ text + " "
#              vys += (((n)//2)*"*")
#          else:
#              vys += (((n)//2)*"*")
#              vys += " "+ text + " "
#              vys += (((n)//2)*"*")
#      else:
#          vys += n*"*"
#      print (vys)
#
# sir = 40
# riadok(sir,"")
# riadok(sir,'Ján Botto')
# riadok(sir,'Žltá ľalija')
# riadok(sir,'-')
# riadok(sir,'Stojí stojí mohyla')
# riadok(sir,'Na mohyle zlá chvíľa')
# riadok(sir,'na mohyle tŕnie chrastie')
# riadok(sir,'a v tom tŕní chrastí rastie')
# riadok(sir,"")
#####

# def uloha1(ret:str)->str:
#     polka = len(ret) //2
#     if len(ret)%2==1:
#         polka +=1
#1cez rezy
#     pp = ret[0:polka:].upper()
#     dp = ret[polka::].lower()
#     return pp+dp
# print(uloha1("jozo"))
#2. bez rezov
#     for i in range(0,polka):
#         pp += ret[i].upper
#     for i in range(polka, len(ret)):
#         hp+= ret[i].lower()
#    return pp+hp
# print(uloha1("jozo"))

#def pigspeech(text):
#     ret = len(text)
#     noveslovo =""
#     if ret>3:
#         noveslovo = text[1::] + text[:1:]
#         noveslovo += "ya"
#     else:
#         noveslovo = text
#     return noveslovo
#print(pigspeech(""))
#
#def accum(text):
#    noveslovo =""
#    for i in range(len(text)):
#        temp = text[i]*(i+1)
#        temp = temp.capitalize()
#        temp += "-"
#        noveslovo += temp
#    return noveslovo[:-1:]
#
#
#print(accum("tomas"))
