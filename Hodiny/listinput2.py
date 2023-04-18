def nakup(zoznam):
    sum = 0
    for i in range (0,len(zoznam),2):
        product = zoznam[i]*zoznam[i+1]
        sum += product
    return sum
