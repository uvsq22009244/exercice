import tkinter as tk
import random as rd


demarrer = 1

def start(balle):
    global demarrer
    if demarrer:
        mouvement(balle)
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    demarrer = 1 - demarrer

def creer_balle():
    """blabla"""
    x, y = 300, 200
    r = 20
    cercle = canvas.create_oval((x-r, y-r), (x+r, y+r), fill="blue")
    n1 = rd.randint(1, 7)
    n2 = rd.randint(1, 7)
    return [cercle, n1, n2]


def mouvement(balle):
    """blabla"""
    global id_after
    balle = rebond1(balle)
    canvas.move(balle[0], balle[1], balle[2])
    id_after = canvas.after(20, lambda: mouvement(balle))


def rebond_horizontal(balle):
    """blabla"""
    x0, y0, x1, y1 = canvas.coords(balle[0])
    return x0 <= 0 or x1 >= 600


def rebond_vertical(balle):
    """blabla"""
    x0, y0, x1, y1 = canvas.coords(balle[0])
    return y0 <= 0 or y1 >= 400


def rebond1(balle):
    """blabla"""
    if rebond_horizontal(balle):
        balle[1] = -balle[1]
    if rebond_vertical(balle):
        balle[2] = -balle[2]
    return balle


# programme prinicipal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
balle = creer_balle()
bouton = tk.Button(racine, text="Démarrer", command=lambda: start(balle))
bouton.grid()

racine.mainloop()