import pandas


# on charge un fichier en fonction de son extension 
def load_file(filepath):
  
    if filepath.endswith('.csv'):
        df = pandas.read_csv(filepath)  # chargement d'un fichier csv
    elif filepath.endswith('.xlsx'):
        df = pandas.read_excel(filepath, sheet_name='excel_file')  # chargement d'un fichier Excel avec une feuille spécifique
    elif filepath.endswith('.json'):
        print("C'est un fichier JSON.")
        df = pandas.read_json(filepath)  # chargement d'un fichier JSON
    elif filepath.endswith('.html'):
        df = pandas.read_html(filepath)[0]  # on retourne une liste de datframes
    else:
        raise ValueError("le format du fichier n'est pas supporte")  # erreur si le format n'est pas reconnu
    
    return df


df_json = load_file('json.json')  
print("contenu du fichier JSON :")
print(df_json)



# on filtre les lignes où la colonne "boolean" = "Yes"
def filter_by_boolean(df, column_name="boolean", value="Yes"):
    filtered_df = df[df[column_name] == value]
    print(f"nombre de lignes filtrees ou {column_name} = {value} : {len(filtered_df)}")
    return filtered_df



#  on filtre les lignes où la colonne "url" contient "reddit"
def filter_by_url(df, column_name="url", substring="reddit"):
    filtered_df = df[df[column_name].str.contains(substring, case=False, na=False)]
    print(f"nombre de lignes filtrees où {column_name} contient '{substring}' : {len(filtered_df)}")
    return filtered_df


# on calcule le pourcentage de lignes respectant au moins une des deux conditions
def compute_percentage(df, col_bool="boolean", val_bool="Yes", col_url="url", val_url="reddit"):
    total_rows = len(df)
    if total_rows == 0:
        return 0  # Retourne 0% si le DataFrame est vide

    condition1 = df[col_bool] == val_bool
    condition2 = df[col_url].str.contains(val_url, case=False, na=False)

    filtered_rows = df[condition1 | condition2]

    percentage = (len(filtered_rows) / total_rows) * 100
    print(f"pourcentagfe de lignes respectant au moins une condition : {percentage:.2f}%")
    return percentage


# on sauvegarde les fichiers filtrés
def save_filtered_data(df, filename_boolean="filtered_boolean.csv", filename_url="filtered_url.csv"):
    df_boolean = filter_by_boolean(df)
    df_url = filter_by_url(df)

    df_boolean.to_csv(filename_boolean, index=False)
    df_url.to_csv(filename_url, index=False)

    print(f"les fichiers filtres ont été sauvegardes :\n- {filename_boolean} ({len(df_boolean)} lignes)\n- {filename_url} ({len(df_url)} lignes)")


file_path = 'json.json'

# on charge le fichier
df = load_file(file_path)

# on vérifie si le fichier contient bien les colonnes nécessaires
if "boolean" in df.columns and "url" in df.columns:
    # on test les fonctions
    filter_by_boolean(df)
    filter_by_url(df)
    compute_percentage(df)
    save_filtered_data(df)
else:
    print("Les colonnes 'boolean' et 'url' sont manquantes dans le fichier.")