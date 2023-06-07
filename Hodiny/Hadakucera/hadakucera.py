import tkinter as tk

win = tk.Tk()

width = 500
height = 500

canvas = tk.Canvas(win,width=width,height=height,)
canvas.pack()
head = [500//2,500//2]
vector = [0,-1]
speed = 100
def draw_snake():
    global head,vector,speed
    canvas.create_rectangle(head[0],head[1],head[0],head[1],fill="black")
    overlap = canvas.find_overlapping(head[0],head[1],head[0],head[1])
    head[0] += vector[0]
    head[1] += vector[1]
    if len(overlap)>1:
        canvas.delete("all")
        canvas.create_text(500//2,500//2,text="you lost")
    else:
        canvas.after(speed,draw_snake)


def changer(e):
    global vector,speed
    if e.char =="w":
        vector = [0,-1]
    elif e.char =="d":
        vector = [1,0]
    elif e.char =="a":
        vector = [-1,0]
    elif e.char == "s":
        vector = [0,1]
    elif e.char == "k" and speed>=1:
        speed -=10
    elif e.char == "l":
        speed +=10















draw_snake()

win.bind("<KeyPress>",changer)

win.mainloop()
