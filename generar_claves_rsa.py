from Crypto.PublicKey import RSA

def main():
    clave = RSA.generate(2048)

    clave_privada = clave.export_key()

    clave_publica = clave.publickey().export_key()

    with open("medisoft_priv.pem", "wb") as archivo_priv:

        archivo_priv.write(clave_privada)

    with open("medisoft_pub.pem", "wb") as archivo_pub:

        archivo_pub.write(clave_publica)

    print("Clave privada guardada en medisoft_priv.pem")

    print("Clave publica guardada en medisoft_pub.pem")


if __name__ == "__main__":
    main()