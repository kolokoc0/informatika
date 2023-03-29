import tkinter as tk

win = tk.Tk()
def mover():
    #kan
    canvas.move(obdlznik1,5,0) #pohne sa o 5
    canvas.after(1,mover) #pocka 1000 ms a zavola sa znovu




def drticka(e): #e je misticky parameter
    print("vykonala som sa")
    print(e.x,e.y) #printe suradnice kde kliknem
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)  #hladam ci nieco overlapuje so stvorcekom 1x1 ktory je tam kde kliknem, zisti ktore objekty lezia na danej ploche
    print(zozob)
    if 1 in zozob:
        print("Tukol som na stvorec")
        a = canvas.itemcget(obdlznik1,"fill")
        if a == "red":
            canvas.itemconfig(obdlznik1,fill="turquoise")
        else:
            canvas.itemconfig(obdlznik1,fill="red")
        canvas.move(obdlznik1,5,5)
def naspat(e):
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in zozob:
        canvas.move(obdlznik1,-20,0) #movujem naspat
canvas = tk.Canvas(win,width = 500,height =500,bg="white")
canvas.pack()

obdlznik1 = canvas.create_rectangle(50,50,250,250,fill="turquoise",tags="idk")
kruznica = canvas.create_oval(180,180,500,500,fill="maroon1")

canvas.bind("<Button-1>",drticka)  #to button je udalost a na to je zoznam udalosti na internete (netreba pamatat, ale treba aspon poznat ake existuju)
canvas.bind("<Button-3>",naspat) #button-2 je tlacido na koliecku -- canvas.bind k pozadovanej udalosti na kanvase pripne nejaku akciu - da sa aj na dany utvar

mover()















print(obdlznik1) #ked to printnem tak mi to ukaze id objektu pri tomto 1


#kazdemu objektu dokazem priradit nejaku znacku cez tags a potom sa pytat na tie tagy





















win.mainloop()
