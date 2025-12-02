import time
MASTER_PASSWORD = "1234"  # Le mot de passe maître

# Liste de mots de passe
passwords = {
    "Instagram": "insta2025!",
    "Snapchat": "snap-super123",
    "Gmail": "gmailPass#44"
}

print("Bienvenue")
print("Veuillez entrer le code pour votre gestionnaire de mots de passe :")

tentatives = 0  # Compteur d'essais ratés

while True:
    entree = input()  # L'utilisateur tape le mot de passe

    if entree == MASTER_PASSWORD:
        print("Oui, c'est le bon mot de passe.\n")
        print("Voici vos mots de passe :\n")
        for site, mdp in passwords.items():
            print(f"{site} : {mdp}")
        break

    else:
        tentatives += 1
        print("Mot de passe incorrect. Veuillez réessayer :")

        # Si 3 tentatives ratées → pause 10 secondes
        if tentatives == 3:
            print("\nTrop de tentatives. Blocage pendant 10 secondes...\n")
            time.sleep(10)
            tentatives = 0  # On remet à zéro après le blocage
            print("Vous pouvez réessayer :")

