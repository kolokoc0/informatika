import tkinter

win = tkinter.Tk() #z balicka vytvorim okno (konstruktor)


#def executor(): #ten parameter executor(e) to e je objekt ktory ked napr kliknes misou tak tam budu suradnice moze tam byt hocico
                # --- tu to nemusi byt ale mozno v buducnosti
    #print("People who die are dead.")

#button = tk.Button(win,text = "Click me !!",command = executor)
#button.pack() #tento sposob dava komponenty pod seba
at = tkinter.Label(win,text = "koeficient a:")
at.pack()
a = tkinter.Entry(win)
a.pack()
bt = tkinter.Label(win,text = "koeficient b:")
bt.pack()
b = tkinter.Entry(win)
b.pack()
ct = tkinter.Label(win,text = "koeficient c:")
ct.pack()
c = tkinter.Entry(win)
c.pack()