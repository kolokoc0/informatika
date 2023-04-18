import tkinter as tk

win = tk.Tk() #z balicka vytvorim okno (konstruktor)


#def executor(): #ten parameter executor(e) to e je objekt ktory ked napr kliknes misou tak tam budu suradnice moze tam byt hocico
                # --- tu to nemusi byt ale mozno v buducnosti
    #print("People who die are dead.")

#button = tk.Button(win,text = "Click me !!",command = executor)
#button.pack() #tento sposob dava komponenty pod seba
at = tk.Label(win,text = "koeficient a:")
at.pack()
a = tk.Entry(win)
a.pack()
bt = tk.Label(win,text = "koeficient b:")
bt.pack()
b = tk.Entry(win)
b.pack()
ct = tk.Label(win,text = "koeficient c:")
ct.pack()
c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get())
    a_koe = float(a.get())
    b_koe = float(b.get())
    c_koe = float(c.get())
    diskriminant = (b_koe**2) - (4*a_koe*c_koe)
    if diskriminant <0:
        nr = "Nema riesenie v R"
        ries = tk.Label(win, text = nr)
        ries.pack()
    elif diskriminant==0:
        jr = "Koren je: " + str(-1*b_koe/(2*a_koe))
        ries = tk.Label(win, text = jr)
        ries.pack()
    else:
        x1 = ((-1*b_koe+diskriminant**0.5)/(2*a_koe))
        x2 = ((-1*b_koe-diskriminant**0.5)/(2*a_koe))
        ries = tk.Label(win, text = ("Riesenie x1: " + str(x1) + "| Riesenie x2: " +str(x2) ))
        ries.pack()




button = tk.Button(win,text = "Click me !!",command = executor)
button.pack()











win.mainloop()  #loop - ako keby program stale isiel v cykle aby mohol zachytavat eventy v okne - vzdy na konci

