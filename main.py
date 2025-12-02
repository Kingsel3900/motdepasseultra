MASTER_PASSWORD = "1234"  # Le mot de passe maitre

# Liste de mots de passe
passwords = {
    "Instagram": "insta2025!",
    "Snapchat": "snap-super123",
    "Gmail": "gmailPass#44"
}

print("Bienvenue")
print("Veuillez entrer le code pour votre gestionnaire de mots de passe :")

while True:
    entree = input() 

    if entree == MASTER_PASSWORD:
        print("Oui, c'est le bon mot de passe.\n")
        print("Voici vos mots de passe :\n")
        for site, mdp in passwords.items():
            print(f"{site} : {mdp}")
        break
    else:
        print("Mot de passe incorrect. Veuillez ressayer :")
