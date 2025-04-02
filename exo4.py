import os
import shutil
from datetime import datetime
import sys

# 1. Lister le contenu du dossier et créer une copie du fichier avec la date et l'heure dans le nom
def lister_contenu_et_copier_fichier(dossier_travail, fichier_a_copier):
    # Lister le contenu du dossier
    print(f"Contenu du dossier {dossier_travail}:")
    for item in os.listdir(dossier_travail):
        print(item)

    # Créer la copie du fichier avec la date et l'heure dans le nom
    date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier_copie = f"{fichier_a_copier}_{date_heure}"
    chemin_fichier_a_copier = os.path.join(dossier_travail, fichier_a_copier)
    chemin_fichier_copie = os.path.join(dossier_travail, nom_fichier_copie)
    
    # Copier le fichier si il existe
    if os.path.exists(chemin_fichier_a_copier):
        shutil.copy(chemin_fichier_a_copier, chemin_fichier_copie)
        print(f"Fichier copié sous le nom {nom_fichier_copie}")
    else:
        print(f"Le fichier {fichier_a_copier} n'existe pas dans le dossier {dossier_travail}.")

# 2. Compter le nombre de fichiers dans un dossier de travail
def compter_fichiers(dossier_travail):
    compteur = 0
    # Vérifier que le dossier existe
    if os.path.isdir(dossier_travail):
        # Parcourir les éléments du dossier
        for item in os.listdir(dossier_travail):
            item_path = os.path.join(dossier_travail, item)
            # Vérifier si l'élément est un fichier
            if os.path.isfile(item_path):
                compteur += 1
        print(f"Il y a {compteur} fichiers dans le dossier {dossier_travail}.")
    else:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")

# 3. Passer un argument pour compter les fichiers dans un dossier donné
def compter_fichiers_arg(dossier_travail):
    compteur = 0
    # Vérifier que le dossier existe
    if os.path.isdir(dossier_travail):
        # Parcourir les éléments du dossier
        for item in os.listdir(dossier_travail):
            item_path = os.path.join(dossier_travail, item)
            # Vérifier si l'élément est un fichier
            if os.path.isfile(item_path):
                compteur += 1
        print(f"Il y a {compteur} fichiers dans le dossier {dossier_travail}.")
    else:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")

# Fonction principale pour exécuter selon les besoins
if __name__ == "__main__":
    # Exemple d'utilisation de lister_contenu_et_copier_fichier
    # Lister le contenu du dossier et copier un fichier avec la date et l'heure
    dossier_travail = "./"  # Utiliser le dossier de travail actuel
    fichier_a_copier = "example.txt"  # Nom du fichier à copier
    lister_contenu_et_copier_fichier(dossier_travail, fichier_a_copier)

    # Exemple d'utilisation de compter_fichiers
    # Compter les fichiers dans le dossier de travail
    compter_fichiers(dossier_travail)

    # Exemple d'utilisation de compter_fichiers_arg
    # Vérifier si un chemin est passé en argument
    if len(sys.argv) > 1:
        chemin_dossier = sys.argv[1]
        compter_fichiers_arg(chemin_dossier)
    else:
        print("Veuillez fournir un chemin de dossier en argument.")
