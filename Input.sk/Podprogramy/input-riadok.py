def riadok(n,text):
    vys = ""
    dlzte = len(text)
    if text!="":
      if dlzte%2==0:
            n -= (dlzte+2)
            vys += (((n)//2)*"*")
            vys += " "+ text + " "
            vys += (((n)//2)*"*")
      else:
        n -= (dlzte+2)
        vys += (((n)//2)*"*")
        vys += " "+ text + " "
        vys += ((((n)//2)+1)*"*")
    else:
        vys += n*"*"
    print (vys)
sir = 40
riadok(sir, "")
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir, "")
