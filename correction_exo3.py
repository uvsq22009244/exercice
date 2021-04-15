import random as rd
import copy as cp


def creer_tableau(n):
    """Retourne un tableau de taille nxn avec des 0 sur les bords
        et des valeurs choisies au hasard entre 5 et 9 ailleurs"""
    tableau = [[0]*n for i in range(n)]
    for i in range(1, n-1):
        for j in range(1, n-1):
            tableau[i][j] = rd.randint(5, 9)
    return tableau


def afficher_tableau(tab):
    """Affiche un tableau"""
    n = len(tab)
    print("###################")
    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print()


def afficher_tableau_somme(tab):
    """Affiche le tableau avec les sommes sur les lignes et colonnes"""
    n = len(tab)
    print("###################")
    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=" ")
        print("*", sum(tab[i]))
    for i in range(n):
        print("**", end="")
    print()
    for j in range(n):
        col = [tab[i][j] for i in range(n)]
        print(sum(col), end=" ")
    print()


def etape_parallele(tab):
    """Fait une étape de l'automate parallèle"""
    cont = False
    tab_res = cp.deepcopy(tab)
    n = len(tab)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if tab[i][j] >= 4:
                cont = True
                tab_res[i][j] -= 4
                tab_res[i+1][j] += 1
                tab_res[i-1][j] += 1
                tab_res[i][j+1] += 1
                tab_res[i][j-1] += 1
    return tab_res, cont


def automate_parallele(tab):
    """Exécute l'automate jusquà stabilisation"""
    while True:
        tab, cont = etape_parallele(tab)
        if not cont:
            break
    return tab


tableau = creer_tableau(5)
print("Affichage du tableau")
afficher_tableau(tableau)
print("Affichage du tableau avec les sommes")
afficher_tableau_somme(tableau)
print("Affichage du tableau après exécution de l'automate parallèle")
afficher_tableau_somme(automate_parallele(tableau))
