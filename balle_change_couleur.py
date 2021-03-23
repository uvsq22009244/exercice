import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)

def est_dans_cercle(x, y):
    """Retourne True si le point de coordonées (x,y) est dans le cercle,
     et False sinon"""
    return 0 < x < 600 and 0 < y < 400

#cpt = 0
#def change_couleur(event):
    """Change la couleur du cercle lorsqu'on clique dans le canevas"""
  #  global cpt
  #  rebond()
   # liste_couleur = ["blue", "red"]
    #if est_dans_cercle(event.x, event.y):
        # si on a cliqué dans la canevas
     #   canvas.itemconfigure(balle[0], fill=liste_couleur[cpt])
      #  cpt = (cpt + 1) % 2
        # alternative
        # cpt = 1 - cpt

cpt = 0
def change_couleur():
    global cpt
    rebond()
    x0, y0, x1, y1 = canvas.coords(balle[0])
    liste_couleur = ["blue", "red"]
    if x0 <= 0 or x1 >= 600 and y0 <= 0 or y1 >= 400 :
        #balle[1] = -balle[1]
        canvas.itemconfigure(balle[0], fill=liste_couleur[cpt])
        cpt = (cpt + 1) % 2
    #if y0 <= 0 or y1 >= 400:
        #balle[2] = -balle[2]
        #canvas.itemconfigure(balle[0], fill=liste_couleur[cpt])
        #cpt = (cpt + 1) % 2
    #return change_couleur

def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]


######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
balle = creer_balle()
mouvement()
change_couleur()

#canvas.bind("<Button-1>", change_couleur)
racine.mainloop()
