import os
import glob
import zipfile
from datetime import datetime
import shutil
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

def format_size(size_bytes):
    """Formatea el tamaño en bytes a MB o GB según sea más legible"""
    size_mb = size_bytes / (1024 * 1024)
    if size_mb >= 1024:
        return f"{size_mb/1024:.2f} GB"
    return f"{size_mb:.2f} MB"

def select_directory(title, initial_dir=None):
    """Muestra un diálogo para seleccionar directorio"""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    if initial_dir is None:
        initial_dir = os.getcwd()
    
    path = filedialog.askdirectory(
        title=title,
        initialdir=initial_dir
    )
    
    return path if path else initial_dir

# Solicitar rutas usando diálogos nativos
print("ATM10 Server Backup Tool")
print("-" * 50)

server_path = select_directory("Selecciona la carpeta del servidor ATM10")
if not server_path:
    print("No se seleccionó ninguna carpeta. Usando directorio actual.")
    server_path = os.getcwd()
  
print(f"Directorio del servidor: {server_path}")

backup_path = select_directory("Selecciona la carpeta para guardar los backups", 
                             os.path.dirname(server_path))
if not backup_path:
    print("No se seleccionó carpeta de backup. Usando <servidor>_BACKUPS")
    backup_path = f"{server_path}_BACKUPS"

date = datetime.now().strftime("%Y-%m-%d_%H-%M")
backup_name = f"minecraft_backup_{date}.zip"

# Crear directorio de backups si no existe
os.makedirs(backup_path, exist_ok=True)

# Encontrar el instalador de neoforge actual
neoforge_installer = glob.glob(os.path.join(server_path, "neoforge-*-installer.jar"))
if not neoforge_installer:
    print("Error: No se encontró el instalador de neoforge en el directorio")
    exit(1)
neoforge_installer = os.path.basename(neoforge_installer[0])

# Lista de archivos y carpetas a respaldar
items_to_backup = [
    "config",
    "defaultconfigs",
    "kubejs",
    "mods",
    "packmenu",
    neoforge_installer,
    "server-icon.png",
    "startserver.bat",
    "startserver.sh",
    "user_jvm_args.txt",
    "world",
    "server.properties",
    "whitelist.json",
    "ops.json",
    "banned-players.json",
    "banned-ips.json"
]

# Crear el archivo zip
backup_full_path = os.path.join(backup_path, backup_name)
print(f"\nCreando backup en: {backup_full_path}")

# Obtener lista total de archivos a comprimir y calcular tamaño total
total_files = []
total_size = 0
for item in items_to_backup:
    item_path = os.path.join(server_path, item)
    if os.path.exists(item_path):
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            total_files.append((item_path, item, size))
            total_size += size
        else:
            for root, _, files in os.walk(item_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, server_path)
                    size = os.path.getsize(file_path)
                    total_files.append((file_path, arcname, size))
                    total_size += size

# Mostrar progreso de compresión
print(f"\nComprimiendo {len(total_files)} archivos ({format_size(total_size)})...")

processed_size = 0
with zipfile.ZipFile(backup_full_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        for file_path, arcname, size in total_files:
            try:
                zipf.write(file_path, arcname)
                pbar.update(size)
            except Exception as e:
                print(f"\nError al comprimir {arcname}: {str(e)}")

backup_size = os.path.getsize(backup_full_path)
print(f"\nBackup completado exitosamente:")
print(f"Nombre: {backup_name}")
print(f"Archivos comprimidos: {len(total_files)}")
print(f"Tamaño original: {format_size(total_size)}")
print(f"Tamaño comprimido: {format_size(backup_size)}")
print(f"Ratio de compresión: {(backup_size/total_size*100):.1f}%")
print(f"Ubicación: {backup_path}")
