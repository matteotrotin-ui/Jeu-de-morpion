def afficher_grille(grille):
    print("\n")
    for i in range(3):
        print(" | ".join(grille[i]))
        if i < 2:
            print("-" * 5)
    print("\n")


def verifier_gagnant(grille, joueur):
    # Vérifie lignes
    for ligne in grille:
        if ligne.count(joueur) == 3:
            return True

    # Vérifie colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] == joueur:
            return True

    # Vérifie diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True

    return False


def morpion():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"
    coups = 0

    while True:
        afficher_grille(grille)
        print(f"Au tour du joueur {joueur} :")

        try:
            ligne = int(input("Choisis une ligne (0, 1, 2) : "))
            colonne = int(input("Choisis une colonne (0, 1, 2) : "))
        except ValueError:
            print("Entrée non valide, recommence.")
            continue

        if ligne not in range(3) or colonne not in range(3):
            print("Position incorrecte, recommence.")
            continue

        if grille[ligne][colonne] != " ":
            print("Case déjà occupée, recommence.")
            continue

        grille[ligne][colonne] = joueur
        coups += 1

        if verifier_gagnant(grille, joueur):
            afficher_grille(grille)
            print(f"🎉 Le joueur {joueur} a gagné !")
            break

        if coups == 9:
            afficher_grille(grille)
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"


if __name__ == "__main__":
    morpion()
