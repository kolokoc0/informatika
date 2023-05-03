import random
import tkinter as tk

win = tk.Tk()

width = 400
height = 400

circle = 30

rect_size = 20

x = 1
y = 1

d = 2

vector = [1*d,1*d]

canvas = tk.Canvas(win,width = width,height = height,bg ="white")
canvas.pack()

gulicka = canvas.create_oval(245,10,245+circle,10+circle,fill="red")

platform = canvas.create_rectangle(150,360,250,360+rect_size,fill="black")

def vectors():
    num = random.randint(-1,1)
    print(num)
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



def movement():
    vector = vectors()
    canvas.move(gulicka,vector[0],vector[1])
    canvas.after(10,movement)




def rightmove():
    canvas.move(platform,1,0)
    print("right")
def leftmove():
    canvas.move(platform,-1,0)
    print("left")

canvas.bind("<Left>",leftmove)
canvas.bind("<Right>",rightmove)


movement()

win.mainloop()
