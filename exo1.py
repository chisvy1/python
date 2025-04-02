# Question 1 : Demander à l'utilisateur une adresse IPv4
def demander_ip_v4():
    """
    Demande à l'utilisateur d'entrer une adresse IPv4.
    Retourne l'adresse IP entrée par l'utilisateur.
    """
    ip = input("Veuillez entrer une adresse IPv4 : ")
    return ip

# Question 2 : Vérifier si l'adresse IPv4 est valide
def verifier_ip_v4(ip):
    """
    Vérifie si l'adresse IPv4 est valide.
    Chaque octet doit être un nombre entier entre 0 et 255.
    Retourne True si l'adresse est valide, False sinon.
    """
    octets = ip.split(".")  # Découpe l'adresse en octets
    
    if len(octets) != 4:  # Vérifie qu'il y a bien 4 octets
        return False
    
    for octet in octets:
        try:
            val = int(octet)  # Convertir chaque octet en entier
            if val < 0 or val > 255:  # Vérifie que chaque octet est entre 0 et 255
                return False
        except ValueError:  # Si l'octet n'est pas un entier valide
            return False
            
    return True

# Question 3 : Vérifier si l'adresse IPv6 est valide
def verifier_ip_v6(ip):
    """
    Vérifie si l'adresse IPv6 est valide.
    Chaque groupe doit être composé de 1 à 4 caractères hexadécimaux (0-9, a-f).
    Retourne True si l'adresse est valide, False sinon.
    """
    groupes = ip.split(":")  # Découpe l'adresse en groupes
    
    if len(groupes) != 8:  # Vérifie qu'il y a bien 8 groupes
        return False
    
    for groupe in groupes:
        if len(groupe) == 0 or len(groupe) > 4:  # Vérifie la longueur des groupes
            return False
        try:
            int(groupe, 16)  # Convertir chaque groupe en base 16
        except ValueError:  # Si un groupe ne peut pas être converti en hexadécimal
            return False
            
    return True

# Question 4 : Détecter la version de l'adresse IP (IPv4 ou IPv6)
def detecter_version_ip(ip):
    """
    Détecte si l'adresse est une IPv4 ou IPv6 et retourne la version.
    Retourne 4 pour IPv4, 6 pour IPv6 et 0 pour une adresse invalide.
    """
    if verifier_ip_v4(ip):  # Vérifie si c'est une adresse IPv4 valide
        return 4
    elif verifier_ip_v6(ip):  # Vérifie si c'est une adresse IPv6 valide
        return 6
    else:
        return 0  # Si l'adresse n'est ni IPv4 ni IPv6 valide, retourne 0

# Question 5 : Vérifier une liste d'adresses IP (IPv4 ou IPv6)
def verifier_liste_ips(liste_ips):
    """
    Vérifie une liste d'adresses IP et retourne une liste de tuples contenant
    l'adresse et sa version (4, 6 ou 0 si invalide).
    """
    resultats = []
    
    for ip in liste_ips:
        version = detecter_version_ip(ip)
        resultats.append((ip, version))  # Ajoute le résultat à la liste
    
    return resultats

# Question 6 : Vérifier un dictionnaire d'adresses IP
def verifier_dictionnaire_ips(dictionnaire_ips):
    """
    Vérifie un dictionnaire d'adresses IP où les clés sont des hôtes
    et les valeurs des adresses IP. Retourne une liste de tuples (hôte, IP, version).
    """
    resultats = []
    
    for hote, ip in dictionnaire_ips.items():
        version = detecter_version_ip(ip)
        resultats.append((hote, ip, version))  # Ajoute le résultat avec le nom de l'hôte
    
    return resultats


# Exemple d'utilisation pour tester avec des entrées utilisateur

if __name__ == "__main__":
    # Question 1 : Demander à l'utilisateur de saisir une adresse IPv4 et la vérifier
    ip_v4 = demander_ip_v4()  # Entrée de l'utilisateur pour IPv4
    if ip_v4:
        print(f"Adresse IPv4 entrée : {ip_v4}")
        print(f"Adresse IPv4 valide : {verifier_ip_v4(ip_v4)}")
    
    # Question 2 : Demander à l'utilisateur de saisir une adresse IPv6
    ip_v6 = input("Veuillez entrer une adresse IPv6 : ")  # Entrée de l'utilisateur pour IPv6
    if verifier_ip_v6(ip_v6):
        print(f"Adresse IPv6 valide : {ip_v6}")
    else:
        print("Adresse IPv6 invalide.")
    
    # Question 3 : Demander à l'utilisateur de tester la détection de la version IP
    ip = input("Entrez une adresse IP (IPv4 ou IPv6) pour détecter sa version : ")
    version = detecter_version_ip(ip)
    if version == 4:
        print(f"{ip} est une adresse IPv4 valide.")
    elif version == 6:
        print(f"{ip} est une adresse IPv6 valide.")
    else:
        print(f"{ip} est invalide.")
    
    # Question 4 : Test avec une liste d'adresses IP
    print("\nTest avec une liste d'adresses IP :")
    liste_ips = []
    n = int(input("Combien d'adresses IP voulez-vous entrer ? "))
    for _ in range(n):
        ip = input("Entrez une adresse IP (IPv4 ou IPv6) : ")
        liste_ips.append(ip)
    resultats = verifier_liste_ips(liste_ips)
    print("Résultats pour la liste d'adresses IP :", resultats)

    # Question 5 : Test avec un dictionnaire d'adresses IP
    print("\nTest avec un dictionnaire d'adresses IP :")
    dictionnaire_ips = {}
    n = int(input("Combien d'entrées voulez-vous ajouter dans le dictionnaire ? "))
    for _ in range(n):
        hote = input("Entrez le nom de l'hôte : ")
        ip = input("Entrez l'adresse IP (IPv4 ou IPv6) : ")
        dictionnaire_ips[hote] = ip
    resultats_dico = verifier_dictionnaire_ips(dictionnaire_ips)
    print("Résultats pour le dictionnaire d'adresses IP :", resultats_dico)
