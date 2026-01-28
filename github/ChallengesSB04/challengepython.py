#Challenge "C'est plus! C'est moins!"

import random

def jeu_plus_moins():
    print("--- Bienvenue dans le jeu 'C'est plus ! C'est moins !' ---")

    while True: # Boucle principale pour le bonus "Rejouer"
        # 1. Le programme choisit un nombre secret (disons entre 1 et 50)
        nombre_secret = random.randint(1, 50)
        nombre_trouve = False
        tentatives = 0 # Bonus : Compteur de tentatives
        
        print("\nJe pense à un nombre entre 1 et 50.")

        # 2. Boucle tant que le nombre n'est pas trouvé
        while not nombre_trouve:
            try:
                # L'utilisateur doit deviner
                proposition = int(input("Votre proposition : "))
                tentatives += 1 # On augmente le compteur
                
                # Vérification
                if proposition < nombre_secret:
                    print("C'est plus !")
                elif proposition > nombre_secret:
                    print("C'est moins !")
                else:
                    # Le nombre est trouvé
                    print(f"Bravo, vous avez trouvé !")
                    print(f"Nombre de tentatives : {tentatives}") # Bonus : Affichage du score
                    nombre_trouve = True
                    if tentatives <= 5:
                        print("Excellent travail ! Vous êtes un pro du jeu.")
                    else:
                        print("Bien joué ! Mais t'es un noob.")

            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")

        # 3. Bonus : Demander si l'on veut rejouer
        rejouer = input("\nVoulez-vous rejouer ? (oui/non) : ").lower()
        if rejouer != "oui":
            print("Merci d'avoir joué. Au revoir !")
            break # On sort de la boucle principale, le programme s'arrête

# Lancement du jeu
if __name__ == "__main__":
    jeu_plus_moins()