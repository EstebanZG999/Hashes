import hashlib
import sys
from pathlib import Path

if len(sys.argv) < 6:
    print("Uso: python generar_manifiesto.py archivo1 archivo2 archivo3 archivo4 archivo5")
    sys.exit(1)

rutas = sys.argv[1:]

with open("SHA256SUMS.txt", "a", encoding="utf-8") as manifiesto:

    for ruta_str in rutas:

        ruta = Path(ruta_str)

        if not ruta.exists():

            print(f"Error: no existe el archivo '{ruta}'")
            continue

        hash_obj = hashlib.sha256()

        with open(ruta, "rb") as archivo:

            contenido = archivo.read()

            hash_obj.update(contenido)

        hash_hex = hash_obj.hexdigest()

        nombre_archivo = ruta.name

        manifiesto.write(f"{hash_hex} {nombre_archivo}\n")

        print(f"Agregado correctamente: {nombre_archivo}")