import hashlib
import requests

contrasenas = ["admin", "123456", "hospital", "medisoft2024"]


print("=" * 110)
print("\nCONSULTA A HIBP USANDO SHA-1 + K-ANONYMITY")
print("=" * 110)

for contrasena in contrasenas:

    cont_bytes = contrasena.encode('utf-8')

    sha256_hex = hashlib.sha256(cont_bytes).hexdigest()

    sha1_hex = hashlib.sha1(cont_bytes).hexdigest().upper()

    prefix = sha1_hex[:5]
    suffix = sha1_hex[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("Error al consultar la API")
        continue 
    
    contenido = respuesta.text

    lineas = contenido.splitlines()

    apariciones = 0

    for linea in lineas:
        suffix_api, conteo = linea.split(":")

        if suffix_api == suffix:
            apariciones = int(conteo)
            break

    print(f"\nContraseña: {contrasena}")
    print(f"SHA-256: {sha256_hex}")
    print(f"SHA-1: {sha1_hex}")
    print(f"Aparece en filtraciones: {apariciones} veces")