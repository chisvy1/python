import os
import shutil
from datetime import datetime


def lister_contenu(dossier_travail):
    try:
        contenu = os.listdir(dossier_travail)
        print(f"Contenu du dossier {dossier_travail}:")
        for item in contenu:
            print(item)
    except FileNotFoundError:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")

def copier_fichier(dossier_travail, fichier_a_copier):
    try:
        date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nom_fichier_copie = f"{fichier_a_copier}_{date_heure}"
        chemin_fichier_a_copier = os.path.join(dossier_travail, fichier_a_copier)
        chemin_fichier_copie = os.path.join(dossier_travail, nom_fichier_copie)

        if os.path.exists(chemin_fichier_a_copier):
            shutil.copy(chemin_fichier_a_copier, chemin_fichier_copie)
            print(f"Fichier copié sous le nom {nom_fichier_copie}")
        else:
            print(f"Le fichier {fichier_a_copier} n'existe pas dans le dossier {dossier_travail}.")
    except FileNotFoundError:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")

def compter_fichiers(dossier_travail):
    try:
        compteur = 0
        if os.path.isdir(dossier_travail):
            for item in os.listdir(dossier_travail):
                item_path = os.path.join(dossier_travail, item)
                if os.path.isfile(item_path):
                    compteur += 1
            print(f"Il y a {compteur} fichiers dans le dossier {dossier_travail}.")
        else:
            print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")
    except FileNotFoundError:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")



def lister_contenu_et_copier_fichier(dossier_travail, fichier_a_copier):
    try:
        print(f"Contenu du dossier {dossier_travail}:")
        for item in os.listdir(dossier_travail):
            print(item)

        date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nom_fichier_copie = f"{fichier_a_copier}_{date_heure}"
        chemin_fichier_a_copier = os.path.join(dossier_travail, fichier_a_copier)
        chemin_fichier_copie = os.path.join(dossier_travail, nom_fichier_copie)

        if os.path.exists(chemin_fichier_a_copier):
            shutil.copy(chemin_fichier_a_copier, chemin_fichier_copie)
            print(f"Fichier copié sous le nom {nom_fichier_copie}")
        else:
            print(f"Le fichier {fichier_a_copier} n'existe pas dans le dossier {dossier_travail}.")
    except FileNotFoundError:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")

def compter_fichiers(dossier_travail):
    try:
        compteur = 0
        if os.path.isdir(dossier_travail):
            for item in os.listdir(dossier_travail):
                item_path = os.path.join(dossier_travail, item)
                if os.path.isfile(item_path):
                    compteur += 1
            print(f"Il y a {compteur} fichiers dans le dossier {dossier_travail}.")
        else:
            print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")
    except FileNotFoundError:
        print(f"Le dossier {dossier_travail} n'existe pas ou n'est pas accessible.")


class Dossier:
    def __init__(self, chemin_dossier):
        self.chemin_dossier = chemin_dossier

    def copier_fichier(self, fichier_a_copier):
        try:
            print(f"Contenu du dossier {self.chemin_dossier}:")
            for item in os.listdir(self.chemin_dossier):
                print(item)

            date_heure = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nom_fichier_copie = f"{fichier_a_copier}_{date_heure}"
            chemin_fichier_a_copier = os.path.join(self.chemin_dossier, fichier_a_copier)
            chemin_fichier_copie = os.path.join(self.chemin_dossier, nom_fichier_copie)

            if os.path.exists(chemin_fichier_a_copier):
                shutil.copy(chemin_fichier_a_copier, chemin_fichier_copie)
                print(f"Fichier copié sous le nom {nom_fichier_copie}")
            else:
                print(f"Le fichier {fichier_a_copier} n'existe pas dans le dossier {self.chemin_dossier}.")
        except FileNotFoundError:
            print(f"Le dossier {self.chemin_dossier} n'existe pas ou n'est pas accessible.")

    def compter_fichiers(self):
        try:
            compteur = 0
            if os.path.isdir(self.chemin_dossier):
                for item in os.listdir(self.chemin_dossier):
                    item_path = os.path.join(self.chemin_dossier, item)
                    if os.path.isfile(item_path):
                        compteur += 1
                print(f"Il y a {compteur} fichiers dans le dossier {self.chemin_dossier}.")
            else:
                print(f"Le dossier {self.chemin_dossier} n'existe pas ou n'est pas accessible.")
        except FileNotFoundError:
            print(f"Le dossier {self.chemin_dossier} n'existe pas ou n'est pas accessible.")
