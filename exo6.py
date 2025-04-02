import psutil
import platform
import json
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        pass

    def get_system_info(self):
        info = {
            "OS": platform.system(),
            "version": platform.version(),
            "RAM": psutil.virtual_memory()._asdict()  # Utilisation de _asdict() pour obtenir un dictionnaire complet
        }
        return info

    def export_system_info(self, file_path="system_info.json"):
        info = self.get_system_info()
        with open(file_path, "w") as f:
            json.dump(info, f, indent=4)

    # Question 2 : Lire TOUTES les informations de tous les processus de votre ordinateur et les stocker dans un fichier JSON.
    def get_all_processes(self):
        process_list = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
            try:
                process_list.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process_list

    def export_all_processes(self, file_path="processes_info.json"):
        processes = self.get_all_processes()
        with open(file_path, "w") as f:
            json.dump(processes, f, indent=4)

    # Question 3 : Afficher les processus qui consomment plus de 2% de votre RAM.
    def get_high_memory_processes(self, threshold=2.0):
        processes = self.get_all_processes()
        high_memory = [proc for proc in processes if proc.get('memory_percent', 0) > threshold]
        return high_memory

    def export_high_memory_processes(self, threshold=2.0, file_path="high_memory_processes.json"):
        high_memory = self.get_high_memory_processes(threshold)
        with open(file_path, "w") as f:
            json.dump(high_memory, f, indent=4)

if __name__ == "__main__":
    monitor = SystemMonitor()

    # Exécution Question 1
    monitor.export_system_info("system_info.json")

    # Exécution Question 2
    monitor.export_all_processes("processes_info.json")

    # Exécution Question 3
    high_mem = monitor.get_high_memory_processes(threshold=2.0)
    print("Processus consommant plus de 2% de RAM :")
    for proc in high_mem:
        print(proc)
    monitor.export_high_memory_processes(threshold=2.0, file_path="high_memory_processes.json")

    # Question 4 : Le code a été testé sur plusieurs OS (par exemple Windows et Linux).
    # Veillez à ce que psutil soit installé et compatible avec votre OS.
