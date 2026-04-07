import hashlib
from pathlib import Path
import sys

def calcular_sha256(ruta_archivo):
    hash_obj = hashlib.sha256()

    with open(ruta_archivo, "rb") as archivo:

        while True:
            bloque = archivo.read(8192)
            if not bloque:
                break
            hash_obj.update(bloque)

    return hash_obj.hexdigest()

def main():
    if len(sys.argv) > 1:
        ruta_manifiesto = Path(sys.argv[1])

    else:
        ruta_manifiesto = Path("SHA256SUMS.txt")

    if not ruta_manifiesto.exists():

        print(f"Error: no existe el manifiesto '{ruta_manifiesto}'")

        sys.exit(1)

    lineas = ruta_manifiesto.read_text(encoding="utf-8").splitlines()

    correctos= 0

    incorrectos  = 0

    for linea in lineas:
        
        linea = linea.strip()

        if not linea:
            continue

        partes = linea.split(maxsplit=1)

        if len(partes) != 2:
            
            print(f"Línea inválida en el manifiesto: {linea}")
            incorrectos +=1
            
            continue

        hash_esperado, nombre_archivo = partes

        ruta_archivo = Path(nombre_archivo)

        if not ruta_archivo.exists():

            print('No existe la ruta de ese archivo')

            incorrectos += 1
            continue

        hash_calculado = calcular_sha256(ruta_archivo)

        if hash_calculado == hash_esperado:

            print(f"OK: {nombre_archivo}")

            correctos += 1
        else:

            print(f"ERROR: {nombre_archivo}")

            print(f"  Hash esperado : {hash_esperado}")

            print(f"  Hash calculado: {hash_calculado}")
            
            incorrectos += 1

    print("\nResumen final")
    print(f"Correctos: {correctos}")
    print(f"Incorrectos: {incorrectos}")

if __name__ == "__main__":
    main() 