from re import I


a = int(input("Vloz konecnu hranicu uzatvoreneho intervalu"))
sum = 0
for i in range(1,a+1):
    if i%2 ==0:
        sum = i + sum
print (sum)