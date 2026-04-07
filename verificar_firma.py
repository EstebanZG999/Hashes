from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15


def main():
    try:
        with open("medisoft_pub.pem", "rb") as archivo_pub:
            clave_publica = RSA.import_key(archivo_pub.read())

        with open("SHA256SUMS.txt", "rb") as archivo_manifiesto:
            contenido_manifiesto = archivo_manifiesto.read()

        with open("SHA256SUMS.sig", "rb") as archivo_firma:
            firma = archivo_firma.read()

        hash_manifiesto = SHA256.new(contenido_manifiesto)

        verificador = pkcs1_15.new(clave_publica)
        verificador.verify(hash_manifiesto, firma)

        print("Firma valida: SHA256SUMS.txt fue firmado por MediSoft y no ha sido alterado.")

    except (ValueError, TypeError):
        print("Firma invalida: SHA256SUMS.txt fue alterado o la firma no corresponde a la clave publica.")

    except FileNotFoundError as e:
        print(f"Error: no se encontro el archivo requerido -> {e.filename}")


if __name__ == "__main__":
    main()
