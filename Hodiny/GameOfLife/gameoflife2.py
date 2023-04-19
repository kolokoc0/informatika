#Better than game of life v.0.1, easier I guess (For The Eyes)


file = open("input.txt","r")

text = file.readline()
width, height = text.split(" ")
width = int(width)
height = int(height)


def create2Dmap() ->list:
    map = []
    temp = []
    for row in file:
        for char in row:
            if char == "1":
                temp.append(1)
            if char == "0":
                temp.append(0)
        map.append(temp)
        temp = [ ]
    return map


def FindNeighbours(x,y):
    map = create2Dmap()
    count = 0

    if x-1>=0 and y-1>=0 and map[y-1][x-1] == 1:
        count +=1
    if y-1>=0 and map[y-1][x] == 1:
        count +=1
    if y-1>=0 and x+1<= height-1 and map[y-1][x+1] ==1:
        count +=1
    if x-1>=0 and map[y][x-1] == 1:
        count +=1
    if x+1<=width-1 and map[y][x+1] ==1:
        count +=1
    if y+1<=height-1 and x-1>=0 and map[y+1][x-1]==1:
        count+=1
    if y+1<=height-1 and map[y+1][x] ==1:
        count+=1
    if y+1<=height-1 and x+1<=width-1 and map[y+1][x+1] == 1:
        count+=1
    return count


print(FindNeighbours(4,2))
