import tkinter as tk

cpt = 0
continuer = True


def start():
    """Recommencer du début"""
    global cpt, continuer
    canvas.itemconfigure(rectangle, fill="red")
    cpt = 0
    continuer = True


def est_dans_rectangle(x, y):
    """Retourne True si le point de coordonées (x,y) est dans le rectangle,
     et False sinon"""
    return 100 < x < 400 and 100 < y < 400


def change_couleur(event):
    """Change la couleur du rectangle"""
    global cpt, continuer
    liste_couleur = ["blue", "red"]
    if est_dans_rectangle(event.x, event.y) and continuer:
        # si on a cliqué à l'intérieur du rectangle et si on ne s'est pas arrêté
        canvas.itemconfigure(rectangle, fill=liste_couleur[cpt])
        cpt = (cpt + 1) % 2
        # alternative
        # cpt = 1 - cpt
    else:
        # quand on clique en dehors du rectangle
        continuer = False


racine = tk.Tk()
canvas = tk.Canvas(racine, width=500, height=500, bg="black")
canvas.grid(row=0)
bouton = tk.Button(racine, text="Recommencer", command=start)
bouton.grid(row=1)
rectangle = canvas.create_rectangle(100, 100, 400, 400, fill="red")
canvas.bind("<Button-1>", change_couleur)
racine.mainloop()
