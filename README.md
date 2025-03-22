# ATM10 Server Backup Tool

Script de Python para crear backups de servidores Minecraft All The Mods 10 (ATM10). 

## Características

- Comprime todos los archivos esenciales del servidor en un único archivo ZIP
- Interfaz gráfica para selección de carpetas
- Incluye todos los archivos críticos:
  - Configuraciones (config/, defaultconfigs/)
  - Scripts KubeJS
  - Mods
  - Mundo del servidor
  - Archivos de configuración del servidor
  - Listas de jugadores (whitelist, ops, bans)
- Barra de progreso en tiempo real que muestra:
  - Porcentaje completado
  - Velocidad de compresión
  - Tamaño actual/total
  - Tiempo restante estimado
- Muestra estadísticas del backup al finalizar (tamaño original, comprimido, ratio)

## Requisitos

- Python 3.x
- Biblioteca `tqdm` (`pip install tqdm`)
- Biblioteca `tkinter` (incluida con Python)

## Getting Started

1. Asegúrate de tener Python 3.x instalado
   - Puedes descargarlo desde [python.org](https://www.python.org/downloads/)
   - Durante la instalación, marca la opción "Add Python to PATH"

2. Instala la dependencia requerida:
   ```bash
   # Windows
   pip install tqdm

   # Linux/Mac
   pip3 install tqdm
   ```

3. Descarga el script `backup-server.py`
4. Ejecútalo:
   ```bash
   # Windows
   python backup-server.py

   # Linux/Mac
   python3 backup-server.py
   ```

5. Selecciona las carpetas:
   - Primero selecciona la carpeta del servidor ATM10
   - Luego selecciona dónde quieres guardar los backups
   - Si no seleccionas nada, se usará el directorio actual y una carpeta "_BACKUPS"

## Solución de problemas

Si obtienes un error "tqdm module not found", asegúrate de haber instalado la dependencia correctamente:
```bash
# Verifica la instalación
pip show tqdm

# Si no está instalado, instálalo
pip install tqdm
```

## Notas

- Los backups se nombran con la fecha y hora: `minecraft_backup_YYYY-MM-DD_HH-MM.zip`
- El script mostrará estadísticas detalladas al finalizar el backup
- Asegúrate de tener suficiente espacio en disco para el backup
