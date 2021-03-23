import tkinter as tk
import random 
##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt_rebond = 0


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


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, cpt_rebond
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 1 or y1 >= 400:
        balle[2] = -balle[2]
    #if cpt_rebond < 31:
        #cpt_rebond+=1
        #canvas.after(30, mouvement)


def affichage(event):
    """Lors du clic, création de 2 ligne"""
    rebond()
    if event.x < LARGEUR//2 and event.x > 150//3 : 
        canvas.move(ligne1, 1,0) # on déplace la ligne de -10px vers la gauche suivant la largeur et non la hauteur
        canvas.move(ligne2, 1, 0)
    
######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
ligne1 = canvas.create_line((LARGEUR//2, 0), (LARGEUR//2, HAUTEUR), fill= "blue")
ligne2 = canvas.create_line((150, 0), (150, HAUTEUR), fill= "red")
#ligne = [ligne1, ligne2]
canvas.grid()
balle = creer_balle()
mouvement()
canvas.bind("<Button-1>",affichage)
racine.mainloop()
