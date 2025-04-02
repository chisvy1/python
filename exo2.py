def verifier_ip_v4(ip):
    """
    Vérifie si l'adresse IPv4 est valide.
    Chaque octet doit être un entier entre 0 et 255.
    """
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        try:
            val = int(octet)
            if val < 0 or val > 255:
                return False
        except ValueError:
            return False
    return True

def verifier_ip_v6(ip):
    """
    Vérifie si l'adresse IPv6 est valide.
    L'adresse doit être composée de 8 groupes séparés par ':'.
    Chaque groupe doit comporter 1 à 4 chiffres hexadécimaux.
    """
    groupes = ip.split(":")
    if len(groupes) != 8:
        return False
    for groupe in groupes:
        if len(groupe) == 0 or len(groupe) > 4:
            return False
        try:
            int(groupe, 16)
        except ValueError:
            return False
    return True

def detecter_version_ip(ip):
    """
    Détecte la version de l'adresse IP.
    Retourne 4 si l'adresse est une IPv4 valide,
    6 si c'est une IPv6 valide, sinon 0.
    """
    if verifier_ip_v4(ip):
        return 4
    elif verifier_ip_v6(ip):
        return 6
    else:
        return 0

def verifier_dictionnaire_ips_avec_exception(dictionnaire_ips):
    """
    Vérifie un dictionnaire d'adresses IP dont les clés représentent des hôtes et les valeurs des adresses IP.
    Utilise try/except pour gérer d'éventuelles erreurs.
    Pour simuler une erreur, si le nom de l'hôte est "simulate_error", on lève une exception.
    Retourne une liste de tuples (hôte, ip, version) pour chaque entrée.
    """
    resultats = []
    try:
        for hote, ip in dictionnaire_ips.items():
            # Simulation d'erreur pour un hôte spécifique
            if hote == "simulate_error":
                raise ValueError("Erreur simulée pour l'hôte 'simulate_error'")
            version = detecter_version_ip(ip)
            resultats.append((hote, ip, version))
    except Exception as e:
        print("Une erreur est survenue lors de la vérification du dictionnaire IP :", e)
    return resultats


def remplacer_lettres(file_path, lettres):
    """
    Remplace dans le fichier situé à 'file_path' toutes les occurrences 
    des lettres spécifiées dans la liste 'lettres' par 'x'.
    Gère les exceptions FileNotFoundError, OSError et Exception.
    """
    try:
        # Lire le contenu du fichier
        with open(file_path, "r", encoding="utf-8") as f:
            contenu = f.read()
        
        # Pour chaque lettre à remplacer, on remplace par 'x'
        for lettre in lettres:
            contenu = contenu.replace(lettre, 'x')
        
        # Réécrire le contenu modifié dans le fichier
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(contenu)
        
        print("Les remplacements ont été effectués avec succès dans le fichier.")
    except FileNotFoundError:
        print("Erreur : Fichier non trouvé.")
    except OSError as e:
        print("Erreur OS :", e)
    except Exception as e:
        print("Une erreur est survenue :", e)


def fichier_vers_dictionnaire(file_path):
    """
    Lit le contenu d'un fichier texte et stocke chaque ligne dans un dictionnaire 
    au format {1: "ligne 1", 2: "ligne 2", ...}.
    Gère les exceptions lors de la lecture.
    """
    lignes_dict = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lignes = f.readlines()
        # Nettoyage des retours à la ligne et stockage dans le dictionnaire
        for idx, ligne in enumerate(lignes, start=1):
            lignes_dict[idx] = ligne.rstrip("\n")
    except FileNotFoundError:
        print("Erreur : Fichier non trouvé.")
    except OSError as e:
        print("Erreur OS :", e)
    except Exception as e:
        print("Une erreur est survenue :", e)
    return lignes_dict

def afficher_dictionnaire_lignes(lignes_dict):
    """
    Affiche chaque élément du dictionnaire au format :
    Ligne numéro X : Y caractères → "contenu de la ligne X"
    """
    try:
        for numero, ligne in lignes_dict.items():
            print(f"Ligne numéro {numero} : {len(ligne)} caractères → \"{ligne}\"")
    except Exception as e:
        print("Une erreur est survenue lors de l'affichage :", e)

if __name__ == "__main__":
    
    # --- Partie 1 : Test de la vérification du dictionnaire d'IP avec simulation d'erreur ---
    print("=== Test du dictionnaire IP avec simulation d'erreur ===")
    dico_ips = {
        "serveur-1": "192.168.1.1",
        "simulate_error": "2001:db8::ff00:42:8329",  # Cette clé va déclencher une erreur simulée
        "serveur-3": "3.3.3.999"
    }
    resultats_ips = verifier_dictionnaire_ips_avec_exception(dico_ips)
    print("Résultats de vérification (les entrées correctes seront affichées si aucune erreur n'interrompt):")
    print(resultats_ips)
    
    # --- Partie 2 : Remplacer certaines lettres dans un fichier ---
    print("\n=== Remplacement de lettres dans un fichier ===")
    chemin_fichier = input("Entrez le chemin complet du fichier à modifier : ")
    lettres_a_remplacer = input("Entrez les lettres à remplacer, séparées par une virgule (ex: a,d,h): ")
    # On transforme l'entrée en liste en retirant les espaces inutiles
    liste_lettres = [lettre.strip() for lettre in lettres_a_remplacer.split(",")]
    remplacer_lettres(chemin_fichier, liste_lettres)
    
    # --- Partie 3 : Lire le contenu du fichier dans un dictionnaire et l'afficher ---
    print("\n=== Lecture du fichier et affichage de son contenu ===")
    contenu_dict = fichier_vers_dictionnaire(chemin_fichier)
    afficher_dictionnaire_lignes(contenu_dict)
