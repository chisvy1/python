import requests
import csv
import json
import os

# Méthode 1 : Exécuter une requête GET à l'API DictionaryAPI et retourner les données dans un dictionnaire.
def get_word_definition(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if 400 <= response.status_code < 500:
            raise Exception(f"Erreur {response.status_code} : {response.text}")
        response.raise_for_status()
        return response.json()  # Retourne le body de la requête sous forme de dictionnaire.
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête HTTP :", e)
        return {}

# Méthode 2 : Importer un fichier CSV, modifier son contenu et sauvegarder dans un nouveau CSV (sans écraser l'original).
def modify_csv_file(input_csv, output_csv):
    try:
        with open(input_csv, mode="r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ["modif"] if reader.fieldnames else ["modif"]
            rows = []
            for row in reader:
                row["modif"] = "modifié"  # Modification simple.
                rows.append(row)
        with open(output_csv, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Fichier modifié sauvegardé dans : {output_csv}")
    except Exception as e:
        print("Erreur lors de la modification du CSV :", e)

# Méthode 3 : Stocker le contenu d'un fichier texte dans un dictionnaire {1: "ligne 1", ...}.
def fichier_vers_dictionnaire(file_path):
    d = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            d[idx] = line.rstrip("\n")
    except Exception as e:
        print("Erreur lors de la lecture du fichier texte :", e)
    return d

# Méthode 4 : Afficher chaque élément du dictionnaire selon le format demandé.
def print_dict_lines(d):
    try:
        for k, v in d.items():
            print(f"Ligne numéro {k} : {len(v)} caractères → \"{v}\"")
    except Exception as e:
        print("Erreur lors de l'affichage :", e)

# Méthode 5 : Exporter un dictionnaire dans un fichier JSON.
def export_dict_to_json(data, output_json):
    try:
        os.makedirs(os.path.dirname(output_json), exist_ok=True)
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Données exportées en JSON dans : {output_json}")
    except Exception as e:
        print("Erreur lors de l'export JSON :", e)

# Méthode 6 : Exporter un dictionnaire dans un fichier CSV avec des noms de colonnes.
def export_dict_to_csv(data, output_csv):
    try:
        os.makedirs(os.path.dirname(output_csv), exist_ok=True)
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["line_number", "content"])
            for key, value in data.items():
                writer.writerow([key, value])
        print(f"Données exportées en CSV dans : {output_csv}")
    except Exception as e:
        print("Erreur lors de l'export CSV :", e)

# Exemple d'utilisation
if __name__ == "__main__":
    # Requête API : Afficher la définition d'un mot tapé par l'utilisateur.
    mot = input("Entrez un mot pour obtenir sa définition : ")
    definition = get_word_definition(mot)
    print("Définition reçue :", definition)

    # Importer et modifier un fichier CSV.
    input_csv_path = input("Entrez le chemin complet du fichier CSV à importer (dans csv_files) : ")
    output_csv_path = os.path.join(os.path.dirname(input_csv_path), "modifie_" + os.path.basename(input_csv_path))
    modify_csv_file(input_csv_path, output_csv_path)

    # Stocker le contenu d'un fichier texte dans un dictionnaire et l'afficher.
    file_txt = input("Entrez le chemin complet d'un fichier texte à lire : ")
    dictionnaire = fichier_vers_dictionnaire(file_txt)
    print_dict_lines(dictionnaire)

    # Exporter le dictionnaire dans un fichier JSON.
    output_json = os.path.join("json_files", "export.json")
    export_dict_to_json(dictionnaire, output_json)

    # Exporter le dictionnaire dans un fichier CSV.
    output_csv_export = os.path.join("csv_files", "export.csv")
    export_dict_to_csv(dictionnaire, output_csv_export)
