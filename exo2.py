import tkinter as tk


def start():
    pass

def creer_balle() :
    x, y = 300, 200
    r= 20
    canvas.create_oval((x))

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
bouton = tk.Button(racine, text="Demarrer", command=start)
bouton.grid()

racine.mainloop