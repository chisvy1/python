from fabric import Connection

def list_remote_network_interfaces(host, user, password):
   
    try:
        # connexion SSH à ma machine distante
        conn = Connection(host=host, user=user, connect_kwargs={"password": password})

        # on exécute la commande pour récupérer les interfaces réseau (Linux)
        result = conn.run("ip -o link show | awk -F': ' '{print $2}'", hide=True)

        # extraction des noms des interfaces réseau
        interfaces = result.stdout.strip().split("\n")

        print(f"interfaces réseau sur {host} : {interfaces}")
        return interfaces

    except Exception as e:
        print(f"erreur : {e}")
        return []

# connexion a ma vm
network_interfaces = list_remote_network_interfaces("192.168.232.2", "user", "password")
