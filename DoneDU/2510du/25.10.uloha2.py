def cisla(text):
  ciselka = "0123456789"
  pocitadlo = ""
  for i in text:
    if i in ciselka:
      pocitadlo += i
  return len(pocitadlo)


print(cisla("snehulienka a 7 trpazlikov."))
