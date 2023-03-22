import tkinter as tk
# from tkinter import messagebox as mg
win = tk.Tk()

atext = tk.Label(win,text="koeficient a:")
atext.pack()
a = tk.Entry(win)
a.pack()

btext = tk.Label(win,text="koeficient b:")
btext.pack()
b = tk.Entry(win)
b.pack()

ctext = tk.Label(win,text="koeficient c:")
ctext.pack()
c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get()) #print vypise hodnoty do command line, je to string
    # koeficient, menime zo stringu na integer
    ka = int(a.get())
    kb = int(b.get())
    kc = int(c.get())
    d = (kb**2) - (4*ka*kc)
    if d < 0:
        nic = tk.Label(win, text = "Rovnica nema riesenie v R" )
        nic.pack()
    elif d == 0:
        xtext = tk.Label(win, text = "Rovnica ma iba jedno riesenie: x= " + str(-kb/(2*ka)))
        xtext.pack()
    else:
        textt = tk.Label(win, text = "Rovnica ma dve riesenia:")
        textt.pack()
        x1text = tk.Label(win, text = "x1= " + str((-kb + d ** 0.5) / (2*ka)))
        x1text.pack()
        x2text = tk.Label(win, text = "x2= " + str((-kb - d ** 0.5) / (2*ka)))
        x2text.pack()

button = tk.Button(win, text = "vypocitaj!",command=executor)
#prvy parameter je ktoremu oknu to bude platit, 2parameter je text, 3 parameter je co ide robit
button.pack()

win.mainloop()


#du: aby sa vysledky zjavili vo win
