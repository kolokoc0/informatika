def znak (n,text):
  if n>(len(text)-1):
    vys = "Zly index"
  else:
    vys = text[n]
  return vys
print(znak(6,"kamikadze"))
