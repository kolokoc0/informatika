#Better than game of life v.0.1, easier I guess (For The Eyes)
import tkinter as tk
win = tk.Tk()
file = open("input.txt","r")

text = file.readline()
WIDTH, HEIGHT = text.split(" ")
width = 900
height = 900
WIDTH = int(WIDTH)
HEIGHT = int(HEIGHT)

ws = 15
cell_list = []
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
    file.seek(0)
    file.readline()
    return map


def FindNeighbours(x,y,map):
    count = 0

    if x-1>=0 and y-1>=0 and map[y-1][x-1] == 1:
        count +=1
    if y-1>=0 and map[y-1][x] == 1:
        count +=1
    if y-1>=0 and x+1<= WIDTH-1 and map[y-1][x+1] ==1:
        count +=1
    if x-1>=0 and map[y][x-1] == 1:
        count +=1
    if x+1<=WIDTH-1 and map[y][x+1] ==1:
        count +=1
    if y+1<=HEIGHT-1 and x-1>=0 and map[y+1][x-1]==1:
        count+=1
    if y+1<=HEIGHT-1 and map[y+1][x] ==1:
        count+=1
    if y+1<=HEIGHT-1 and x+1<=WIDTH-1 and map[y+1][x+1] == 1:
        count+=1
    return count

#teraz sa pozrem do mapy budem ju prechadzat pre kazde policko sa spytam kolko mas priatelov
# prechadzam cyklus v cykle vrat mi pocet priatelov pri kazdom ak si 2 ci co tak zdochnes ak nieco ine tak zijes ...?

oldmap = create2Dmap()
print(len(oldmap[0]))
newmap = create2Dmap()


def rewrite(oldmap,newmap):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbours = FindNeighbours(x,y,oldmap)
            if oldmap[y][x] == 1:
                if neighbours<2:
                    newmap[y][x] = 0
                elif neighbours ==2 or neighbours ==3:
                    newmap[y][x] = 1
                elif neighbours >2:
                    newmap[y][x] = 0
            if oldmap[y][x] == 0 and neighbours ==3:
                newmap[y][x] = 1

    return newmap



canvas = tk.Canvas(win,width = width,height = height,bg="white")
canvas.pack()


def drawGrid(ws):
    count = height*100//ws
    for i in range(count+1):
        canvas.create_line(0,i*ws,width*100,i*ws)
    count = width*100//ws
    for i in range(count+1):
        canvas.create_line(i*ws,0,i*ws,height*100)
drawGrid(ws)

def drawCells(oldmap, cell_list, ws):
    canvas.delete("all")
    drawGrid(ws)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if oldmap[y][x] ==1:
                canvas.create_oval(x*ws,y*ws,(x+1)*ws,(y+1)*ws,fill="green")


    #print stary matrix
    #vypocitas novy matrix
    #novy hodis do stareho - pomocou dvoch cyklov .copy() nie pretoze
    #novy musim vynulovat
def calculateGenerations():
    global oldmap,newmap
    drawCells(oldmap,newmap,ws)
    newmap = rewrite(oldmap,newmap)
    oldmap =newmap.copy()
    canvas.after(100,calculateGenerations)
calculateGenerations()
win.mainloop()




