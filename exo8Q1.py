import subprocess

def list_network_interfaces():
   
    # on définit la commande en fonction du système d'exploitation
    command = "wmic nic where NetEnabled=true get Name" if subprocess.os.name == 'nt' else "ip -o link show | awk -F': ' '{print $2}'"
    
    # on exécute la commande et on capture la sortie
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # on récupère les lignes de la sortie en filtrant les lignes vides
    interfaces = [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]
    
    # pn supprime le titre "Name" sous Windows
    if subprocess.os.name == 'nt' and interfaces and interfaces[0].lower() == "name":
        interfaces.pop(0)

    return interfaces  # on retourne la liste des interfaces



network_interfaces = list_network_interfaces()
print(network_interfaces)



