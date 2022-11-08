def samohlasky(text):
  temp = ""
  samo= "aeiouy"
  for i in text:
    if i in samo:
      temp = "True"
    else:
      temp ="False"
      return temp
  return temp
print(samohlasky("aaaaauuyou"))
