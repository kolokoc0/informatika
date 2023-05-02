import tkinter as tk 
win = tk.Tk()

file = open("input.txt","r")

line = file.readline()

height,width = line.split(" ")

height = int(height)
width = int(width)

w = 600
h = 600

ws = 15

canvas = tk.Canvas(win, height = h, width = w, bg = "white")
canvas.pack()



value = "none"

def DrawGrid():
    count = h//ws
    for i in range(count):
        canvas.create_line(0,i*ws,w,i*ws)
    count = w//ws
    for i in range(count):
        canvas.create_line(i*ws,0,i*ws,h)
DrawGrid()

def Create2DMap():
    temp = []
    map = []
    for row in file:
        for char in row:
            if char == "1":
                temp.append(1)
            if char =="0":
                temp.append(0)
        map.append(temp)
        temp = [ ]
    file.seek(0)
    file.readline()
    return map


oldmap = Create2DMap()

newmap = Create2DMap()


def FindNeighbours(x,y,oldamp):
    count = 0
    #oldmap [y][x]
    #navrhnem seriu ifov aby to fungovalo
    if x<width-1 and oldmap[y][x+1] == 1:
        count += 1
    if x<width-1 and y<height-1 and oldmap[y+1][x+1] == 1:
        count += 1
    if y<height-1 and oldmap[y+1][x] == 1:
        count += 1
    if x>0 and y<height-1 and oldmap[y+1][x-1] == 1:
        count += 1
    if x>0 and oldmap[y][x-1] == 1:
        count += 1
    if x>0 and y>0 and oldmap[y-1][x-1] == 1:
        count += 1
    if y>0 and oldmap[y-1][x] == 1:
        count += 1
    if x<width-1 and y>0 and oldmap[y-1][x+1] == 1:
        count += 1
    return count

def Rewrite(oldmap, newmap):
    for y in range(height):
        for x in range(width):
            friends = FindNeighbours(x,y,oldmap)
            if oldmap[y][x] == 1:
                if friends == 2 or friends == 3:
                    newmap[y][x] = 1
                elif friends < 2:
                    newmap[y][x] = 0
                elif friends > 3:
                    newmap[y][x] = 0
            elif oldmap[y][x] == 0:
                if friends == 3:
                    newmap[y][x] = 1
    return newmap

def drawCells(oldmap,ws):
    canvas.delete("all")
    DrawGrid()
    for y in range(height):
        for x in range(width):
            if oldmap[y][x] ==1:
                canvas.create_oval(x*ws,y*ws,(x+1)*ws,(y+1)*ws,fill="red")
def automatic():
    global value
    value = "auto"
    canvas.after(100,Generation)
def pushing():
    global value
    value = "pushing"
    Generation()
    return value
def Generation():
    global oldmap,newmap
    drawCells(oldmap,ws)
    newmap = Rewrite(oldmap,newmap)
    for y in range(height):
        for x in range(width):
            oldmap[y][x]= newmap[y][x]
    canvas.update()
    if value=="auto":
        automatic()
        print(value)

button1 = tk.Button(win, text= "Automatic",command = automatic)
button1.pack()
button2 = tk.Button(win, text="Pushing", command= pushing)
button2.pack()








win.mainloop()


