from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15



def main():

    with open("medisoft_priv.pem", "rb") as archivo_priv:

        clave_privada = RSA.import_key(archivo_priv.read())

    with open("SHA256SUMS.txt", "rb") as archivo_manifiesto:

        contenido = archivo_manifiesto.read()

    hash_manifiesto = SHA256.new(contenido)

    firma = pkcs1_15.new(clave_privada).sign(hash_manifiesto)


    with open("SHA256SUMS.sig", "wb") as archivo_firma:

        archivo_firma.write(firma)

    print("Firma generada correctamente en SHA256SUMS.sig")


if __name__ == "__main__":
    main()