
from firebase_admin import credentials, initialize_app, storage
import os

# Initialisation de l'application Firebase
cred = credentials.Certificate(r"cred.json")
initialize_app(cred, {'storageBucket': 'xxxxxxx.appspot.com'}) // champs à modifier

# Informations sur le répertoire et le bucket
source_folder_name = "" // champs à modifier
bucket_name = "xxxxxxx.appspot.com"

# Chemin vers le bureau de l'utilisateur
desktop_path = os.path.join(os.path.expanduser("~"), "Bureau")

# Création du dossier "images" sur le bureau
images_folder_path = os.path.join(desktop_path, "images")
os.makedirs(images_folder_path, exist_ok=True)

# Téléchargement de tous les fichiers dans le répertoire source
bucket = storage.bucket()
blobs = bucket.list_blobs(prefix=source_folder_name)

for blob in blobs:
    # Nom de fichier relatif dans le dossier "images"
    file_name = os.path.basename(blob.name)
    
    # Sauter les blobs sans nom de fichier (par exemple, les dossiers)
    if not file_name:
        continue
    
    # Chemin complet du fichier de destination dans le dossier "images"
    destination_file_name = os.path.join(images_folder_path, file_name)
    
    # Télécharger le fichier
    blob.download_to_filename(destination_file_name)

print("Tous les téléchargements sont terminés avec succès dans le dossier 'images' sur le bureau!")
                                    
