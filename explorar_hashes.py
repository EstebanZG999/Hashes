import hashlib

textos = ["MediSoft-v2.1.0", "medisoft-v2.1.0"]

algoritmos = {
    "MD5": hashlib.md5,
    "SHA-1": hashlib.sha1,
    "SHA-256": hashlib.sha256,
    "SHA3-256": hashlib.sha3_256,
}


filas_tabla = []

sha_256_text = {}

for texto in textos:
    texto_bytes = texto.encode("utf-8")

    for nombre_alg, hash_func in algoritmos.items():

        hash_obj = hash_func(texto_bytes)

        digest_bytes = hash_obj.digest()

        hash_hex = hash_obj.hexdigest()

        len_bits = len(digest_bytes) *8 
        len_hex = len(hash_hex)

        fila = {
            "entrada": texto,
            "algoritmo": nombre_alg,
            "bits": len_bits,
            "hex_len": len_hex,
            "hash": hash_hex,
        }

        filas_tabla.append(fila)

        if nombre_alg == "SHA-256":
            sha_256_text[texto] = hash_hex

print("=" * 120)
print(f"{'Texto':<22} {'Algoritmo':<12} {'Longitud bits':<15} {'Longitud hex':<15} {'Valor hash'}")
print("=" * 120)

for fila in filas_tabla:
    print(
        f"{fila['entrada']:<22} "
        f"{fila['algoritmo']:<12} "
        f"{fila['bits']:<15} "
        f"{fila['hex_len']:<15} "
        f"{fila['hash']}"
    )

print("=" * 120)

hash1 = sha_256_text[textos[0]]
hash2 = sha_256_text[textos[1]]

hash1_int = int(hash1, 16)

hash2_int = int(hash2, 16)

xor_resultado = hash1_int ^ hash2_int


bits_distintos = xor_resultado.bit_count()

print("\nANALISIS DEL EFECTO AVALANCHA")
print("-" * 50)
print(f"SHA-256 de '{textos[0]}': {hash1}")
print(f"SHA-256 de '{textos[1]}': {hash2}")
print(f"Cantidad de bits que cambiaron: {bits_distintos}")