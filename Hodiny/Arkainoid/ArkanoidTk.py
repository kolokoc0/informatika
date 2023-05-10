import random
import tkinter as tk

win = tk.Tk()

width = 500
height = 500

circle = 15

rect_size = 20

x = 1
y = 1

d = 4

vector = [1*d,1*d]

bricks_w = 50
bricks_h = 20
bricks_count_x = 10
bricks_count_y = 5

bricks_list = [ ]

canvas = tk.Canvas(win,width = width,height = height,bg ="white")
canvas.pack()

gulicka = canvas.create_oval(240,250,240+circle,250+circle,fill="red")

platform = canvas.create_rectangle(250,460,350,460+rect_size,fill="black")

colors = ["green","red","blue","yellow","aquamarine"]

def prepare_bricks():
    for y in range(bricks_count_y):
        for x in range(bricks_count_x):
            bricks_list.append(canvas.create_rectangle(x*bricks_w,y*bricks_h,(x+1)*bricks_w,(y+1)*bricks_h,fill=colors[y%4],width = 5,outline= "white"))

def vectors():
    num = random.randint(-1,1)
    global vector
    coordinates = canvas.coords(gulicka)
    if coordinates[2]>=width:
        vector = [-1*d,1*d+num]
    elif coordinates[0]<=0:
        vector = [1*d,-1*d+num]
    elif coordinates[3]>=height:
        vector = [-1*d,-1*d+num]
    elif coordinates[1]<=0:
        vector = [1*d,1*d+num]
    return vector

def destroy_brick():
    global vector
    ball_coords = canvas.coords(gulicka)
    overlap = canvas.find_overlapping(ball_coords[0],ball_coords[1],ball_coords[2],ball_coords[3])
    for i in overlap:
        if i in bricks_list:
            canvas.delete(i)
            bricks_list.remove(i)
            vector = [vector[0]*(-1),vector[1]*(-1)]












def starter(e):
    global x
    x = e.x

def plat_move(e):
    global x
    x2 = e.x
    vector = x2-x
    canvas.move(platform,vector,0)
    x = x2

#def checkkey(e):
    #print("stlacil som")
    #print(e.char)
#def left_move(e):
    #canvas.move(platform,-10,0)
#def right_move(e):
    #canvas.move(platform,10,0)



def movement():
    global vector
    vector = vectors()
    ball_coords = canvas.coords(gulicka)
    overlap = canvas.find_overlapping(ball_coords[0],ball_coords[1],ball_coords[2],ball_coords[3])
    if 2 in overlap:
        vector = [-1*d,-1*d]
    canvas.move(gulicka,vector[0],vector[1])
    canvas.after(10,movement)
    destroy_brick()

canvas.bind("<Button-1>",starter)
canvas.bind("<B1-Motion>",plat_move)
#canvas.focus_set()
#win.bind("<Key>", checkkey)
#win.bind("<Left>",left_move)
#win.bind("<Right>",right_move)

prepare_bricks()
movement()

win.mainloop()
