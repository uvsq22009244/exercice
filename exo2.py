import tkinter as tk
import random

HEIGHT = 500
WIDTH = 500

def affichage(event):
    """Lors du clic, création de 2 ligne"""
    if event.x < WIDTH//2 : 
        canvas.move(ligne1, -10,0) # on déplace la ligne de -10px vers la gauche suivant la largeur et non la hauteur
    elif event.x > WIDTH*2//3 :
        canvas.move(ligne2, 10, 0) # on déplace la ligne de 10px vers la droite suivant la largeur
    else :
        canvas.move(ligne1, -10,0)
        canvas.move(ligne2, 10, 0)
    #canvas.after(900000, affichage)

creer = 1

def restart_pause(ligne):
    """Suspend et restore le programme """
    global creer, ligne1, ligne2
    id_after = canvas.after(20, lambda: affichage(ligne))
    if creer:
        affichage(ligne)
        bouton.config(text="Restart")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Pause")
    creer = 1 - creer

cpt = 0

def ligne_efface():
    """On va éffacer les 2 lignes"""
    global cpt, ligne1, ligne2
    cpt = 1 - cpt # vaut alternativement 0 et 1
    if cpt == 0:
        #ligne1 = canvas.create_line((WIDTH//2, 0), (WIDTH//2,HEIGHT), fill= "blue")
        #ligne2 = canvas.create_line((WIDTH*2//3, 0), (WIDTH*2//3,HEIGHT), fill= "red") 
    #else:
        canvas.delete(ligne1, ligne2)
        canvas.after(60, affichage)

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="white", width= 500, height= 500)
ligne1 = canvas.create_line((WIDTH//2, 0), (WIDTH//2,HEIGHT), fill= "blue")
ligne2 = canvas.create_line((WIDTH*2//3, 0), (WIDTH*2//3,HEIGHT), fill= "red")
liste_ligne = [ligne1, ligne2]

bouton1 = tk.Button(racine, text="Pause", command= restart_pause)
bouton2 = tk.Button(racine, text= "Effacer", command= ligne_efface)


canvas.grid(row=0)
bouton1.grid(row=1)
bouton2.grid(row=2)
#canvas.bind("<Button-1>", creer_ligne)
canvas.bind("<Button-1>",affichage)
#creer_ligne()
ligne_efface()

racine.mainloop()
