import tkinter as tk
import random
win = tk.Tk()
width = 300
sirka = 15
ux = 20
uy = 250
canvas = tk.Canvas(win, width=500,height=500,bg = "white")
canvas.pack()
farby = ["red","green","gray","yellow","blue"]
vyber = 0

def draw_wires():
    global vyber
    canvas.create_text(width/2,uy-200,text = 'Pyrotechnik', fill="Blue")
    canvas.create_text(width/2,uy-190,text ="Vyber jeden kablik", fill = "Blue")
    for i in range(5):
        canvas.create_rectangle(ux,uy+(i*sirka),width,uy+sirka+(i*sirka),fill=farby[i])
    vyber = random.choice(farby)
    print(vyber)




def stlacenie(e):
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    color = canvas.itemcget(overlap,"fill")
    if color == vyber:
        string = canvas.create_text(width/2,uy+50,text ="Vyhral si!!!!",fill="black")
        string.pack()
    else:
        canvas.delete("all")


draw_wires()
canvas.bind("<Button-1>",stlacenie)
win.mainloop()
