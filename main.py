import sys 
import os 
import time
from datetime import datetime

def file_age(file_path):
    lastModif_time = os.path.getmtime(file_path)
    actual_time = time.time()
    return (actual_time - lastModif_time)/86400


def clean_old_files(folder_path, days_limit=10):
    print(f"---Démarrage du nettoyage du dossier: {folder_path}")
    print(f"Limite d'âge: {days_limit} jours et plus.")

    if not os.path.exists(folder_path):
        print(f"Erreur: Le dossier '{folder_path}' n'existe pas")
        return
    

    deleted_count = 0
    skipped_count = 0

    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path,file)
        if os.path.isfile(file_path) and file_age(file_path) >= days_limit:
            os.remove(file_path)
            print(f"Fichier supprimé : {file}")
            deleted_count += 1
        else: 
            skipped_count += 1
    
    print(f"\n--- Fin du nettoyage ---")
    print(f"Fichiers supprimés : {deleted_count}")
    print(f"Fichiers conservés : {skipped_count}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python clean_folder.py <chemin_du_dossier>")
        sys.exit(1)
        
    target_folder = sys.argv[1]
    clean_old_files(target_folder, days_limit=10)
