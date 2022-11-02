tr = 'jano<jansgs>fsdfafsad<fero><miso>dsads<fdfd>h'
def parsovacka (text:str)->str:
     status = True
     nr = ''
     for i in text:
         if i == "<":
             status = False
         if i == ">":
             status = True
         if status == True:
             if i!= ">" :
                 nr += i
             else:
                 nr += " "
     return nr


print(parsovacka(tr))
