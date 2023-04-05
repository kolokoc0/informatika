import tkinter as tk

win = tk.Tk()
x=0
y=0
def stlacenie(e):
    global x,y     #mali by sme sa mu vyhybat - spravy ze zostane aj vonku z funkcie
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in overlap:
        x = e.x
        y = e.y

def mover(e):
    global x,y
    overlap =canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in overlap:
        x2 = e.x
        y2 = e.y
        vektor = (x2-x,y2-y)
        canvas.move(poly,vektor[0],vektor[1])
        x,y = x2,y2
def releaser(e):
    global x,y
    x=0
    y=0



canvas = tk.Canvas(win, width=500, height=500)
canvas.pack()
poly = canvas.create_polygon(10,10,50,80,140,80,fill="turquoise")


canvas.bind("<Button-1>",stlacenie)
canvas.bind("<B1-Motion>",mover)
canvas.bind("<ButtonRelease-1>",releaser)





win.mainloop()
