#Exercie 04

#liste de prénoms
first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]

#demander un prénom à l'utilisateur et l'ajouter à la liste
firstnames = input("Entre ton prénom: ").strip()

#autoriser les majuscules et minuscules
firstnames_lower = firstnames.lower()
first_names_lower = [name.lower() for name in first_names]

#boucle pour vérifier l'accès et si le prénom est dans la liste
if firstnames_lower in first_names_lower:
    print("Accès autorisé, bienvenue", firstnames)
    for name in first_names:
        if name.lower() == firstnames_lower:
            print(name.upper(), "est dans la liste")
else:   
    print("Bonjour", firstnames, "Accès refusé")

#affiche le nombre de prénoms dans la liste
print("Il y a", len(first_names), "personnes autorisées.")

