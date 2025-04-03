import pandas


# on charge un fichier en fonction de son extension 
def load_file(filepath):
  
    if filepath.endswith('.csv'):
        df = pandas.read_csv(filepath)  # chargement d'un fichier csv
    elif filepath.endswith('.xlsx'):
        df = pandas.read_excel(filepath, sheet_name='excel_file')  # chargement d'un fichier Excel avec une feuille spécifique
    elif filepath.endswith('.json'):
        df = pandas.read_json(filepath)  # chargement d'un fichier JSON
    elif filepath.endswith('.html'):
        df = pandas.read_html(filepath)[0]  # on retourne une liste de datframes
    else:
        raise ValueError("le format du fichier n'est pas supporte")  # erreur si le format n'est pas reconnu
    
    return df



# on stocke dans une liste les lignes ou une colonne a une valeur spé
def filter_by_boolean(df, column_name="boolean", value="Yes"):
    filtered_df = df[df[column_name] == value]  # filtrage dataframe
    return filtered_df.to_dict(orient="records")  # conversion en liste de dico
