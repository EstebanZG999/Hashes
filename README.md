# Laboratorio de Hashes

## Descripcion del Proyecto

Este proyecto implementa distintos mecanismos basados en funciones hash para un escenario de seguridad aplicado a la empresa ficticia MediSoft S.A., la cual distribuye software de diagnostico a hospitales en Centroamerica.

El laboratorio cubre cinco areas principales:

- comparacion de algoritmos hash;
- consulta de contrasenas comprometidas;
- verificacion de integridad de archivos mediante SHA-256;
- firma digital de manifiestos con RSA;
- validacion de autenticidad usando clave publica.

El objetivo es demostrar, tanto de forma practica como conceptual, como se utilizan los hashes y las firmas digitales para proteger la integridad de paquetes distribuidos y el almacenamiento seguro de credenciales.

## Objetivos de Aprendizaje

- Explicar las propiedades fundamentales de las funciones hash: unidireccionalidad, determinismo, efecto avalancha y resistencia a colisiones.
- Seleccionar el algoritmo hash correcto segun el caso de uso: SHA-256 para integridad, Argon2id para contrasenas, HMAC-SHA256 para autenticacion de mensajes.
- Implementar verificacion de integridad de archivos usando SHA-256 con Python.
- Demostrar experimentalmente por que MD5 y SHA-1 no deben usarse en sistemas modernos.
- Implementar mecanismos seguros para autenticidad e integridad de artefactos distribuidos.

## Estructura del Proyecto

```text
Hashes/
|-- README.md
|-- explorar_hashes.py
|-- consultar_hibp.py
|-- generar_manifiesto.py
|-- verificar_paquete.py
|-- generar_claves_rsa.py
|-- firmar_manifiesto.py
|-- verificar_firma.py
|-- SHA256SUMS.txt
|-- SHA256SUMS.sig
|-- medisoft_priv.pem
`-- medisoft_pub.pem
```

## Requisitos

- Python 3.10 o superior
- `pip`
- `requests`
- `pycryptodome`

## Instalacion

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Hashes
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

#### En Windows

```bash
.venv\Scripts\activate
```

#### En Linux o macOS

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install requests pycryptodome
```

## Uso

### 1. Comparacion de algoritmos hash

```bash
python explorar_hashes.py
```

### 2. Consulta de contrasenas en HIBP

```bash
python consultar_hibp.py
```

### 3. Generacion del manifiesto de integridad

```bash
python generar_manifiesto.py archivo1.txt archivo2.txt archivo3.txt archivo4.txt archivo5.txt
```

### 4. Verificacion del paquete

```bash
python verificar_paquete.py
```

Opcionalmente, tambien se puede indicar explicitamente el manifiesto:

```bash
python verificar_paquete.py SHA256SUMS.txt
```

### 5. Generacion de claves RSA

```bash
python generar_claves_rsa.py
```

### 6. Firma digital del manifiesto

```bash
python firmar_manifiesto.py
```

### 7. Verificacion de firma digital

```bash
python verificar_firma.py
```

## Ejemplos de Ejecucion

### Ejemplo 1. Salida de `explorar_hashes.py`

```text
========================================================================================================================
Texto                  Algoritmo    Longitud bits   Longitud hex    Valor hash
========================================================================================================================
MediSoft-v2.1.0        MD5          128             32              cac2fe40370e3a68f0a4927c20c75c89
MediSoft-v2.1.0        SHA-1        160             40              3ab92abc44e23465b154e887f90c3a5e0d642c65
MediSoft-v2.1.0        SHA-256      256             64              64942401fe64ac1182bd88326ba7ca57a23ea5d0475653dea996ac15e8e74996
MediSoft-v2.1.0        SHA3-256     256             64              3b0af4c0a9078e2ddc1606313db9206dcb3a4dbf423d78c0cf16929d303e30d2
medisoft-v2.1.0        MD5          128             32              fa386a0d796e388b24cb3302c185a445
medisoft-v2.1.0        SHA-1        160             40              4fe9fa8c97db362ecce61ee6302a92f0505217cd
medisoft-v2.1.0        SHA-256      256             64              ec8d163da33b9832c33fbb2d7cba98f5a7087aa6cbdecc04eb32810b1f1f895e
medisoft-v2.1.0        SHA3-256     256             64              569daf2d0645c0ab6c0a7960cb552f28ac1a222284fa5605ab11cfe0a2dce82c
========================================================================================================================

ANALISIS DEL EFECTO AVALANCHA
--------------------------------------------------
SHA-256 de 'MediSoft-v2.1.0': 64942401fe64ac1182bd88326ba7ca57a23ea5d0475653dea996ac15e8e74996
SHA-256 de 'medisoft-v2.1.0': ec8d163da33b9832c33fbb2d7cba98f5a7087aa6cbdecc04eb32810b1f1f895e
Cantidad de bits que cambiaron: 120
```

### Ejemplo 2. Salida de `consultar_hibp.py`

```text
CONSULTA A HIBP USANDO SHA-1 + K-ANONYMITY

Contrasena: admin
SHA-256: 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
SHA-1: D033E22AE348AEB5660FC2140AEC35850C4DA997
Aparece en filtraciones: 42085691 veces

Contrasena: 123456
SHA-256: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
SHA-1: 7C4A8D09CA3762AF61E59520943DC26494F8941B
Aparece en filtraciones: 209972844 veces

Contrasena: hospital
SHA-256: 8afe3c83decffdf6dc48597a3f1a52be7c6e2b97b4bdf3b15e20a87a1f657f01
SHA-1: 2B2D005E88CE14A4112785BB266B2C0C16BE7EB4
Aparece en filtraciones: 118791 veces

Contrasena: medisoft2024
SHA-256: 78c12e8e24dfd7836c748c33dff2e9150c028d69488f203485e13f4a6daa777c
SHA-1: F80CF41ABF90CAA2EC08527F641C40B4ABFE4DB9
Aparece en filtraciones: 0 veces
```

### Ejemplo 3. Salida de `generar_manifiesto.py`

```text
python generar_manifiesto.py archivo1.txt archivo2.txt archivo3.txt archivo4.txt archivo5.txt

Agregado correctamente: archivo1.txt
Agregado correctamente: archivo2.txt
Agregado correctamente: archivo3.txt
Agregado correctamente: archivo4.txt
Agregado correctamente: archivo5.txt
```

Contenido de `SHA256SUMS.txt`:

```text
96ba06594ad5bd760087ddf6e4b1b944f1dc76a11dd498b076912b43e7b058ef archivo1.txt
f712f484135fdeb97304afa1df7cb5fbb75b80d1eb964ba38b5a12eac1d9e10f archivo2.txt
9f6197776db4ff56d4a07eb4aaae2b5ca6d3865543f4857fd85a28b8a111bd88 archivo3.txt
ebbfc55e107f35a68ae2a75561718383a47b0cffb6987ac1fde0fece41264ea0 archivo4.txt
823635246b5a9b63f25dfd3bf4589d0e0eae4af80345f04aa2276d9d7e9e25af archivo5.txt
```

### Ejemplo 4. Salida de `verificar_paquete.py`

Caso sin alteraciones:

```text
OK: archivo1.txt
OK: archivo2.txt
OK: archivo3.txt
OK: archivo4.txt
OK: archivo5.txt

Resumen final
Correctos: 5
Incorrectos: 0
```

Caso despues de modificar un byte de `archivo1.txt`:

```text
ERROR: archivo1.txt
  Hash esperado : 96ba06594ad5bd760087ddf6e4b1b944f1dc76a11dd498b076912b43e7b058ef
  Hash calculado: 4c22390e737599099833d9ff1a1b75ed0a4fa7f57800cef96f52df8111f4ad62
OK: archivo2.txt
OK: archivo3.txt
OK: archivo4.txt
OK: archivo5.txt

Resumen final
Correctos: 4
Incorrectos: 1
```

### Ejemplo 5. Salida de `generar_claves_rsa.py`

```text
Clave privada guardada en medisoft_priv.pem
Clave publica guardada en medisoft_pub.pem
```

### Ejemplo 6. Salida de `firmar_manifiesto.py`

```text
Firma generada correctamente en SHA256SUMS.sig
```

### Ejemplo 7. Salida de `verificar_firma.py`

Caso con manifiesto intacto:

```text
Firma valida: SHA256SUMS.txt fue firmado por MediSoft y no ha sido alterado.
```

Caso despues de modificar un caracter dentro de `SHA256SUMS.txt`:

```text
Firma invalida: SHA256SUMS.txt fue alterado o la firma no corresponde a la clave publica.
```

Caso en el que se modifica un archivo del paquete, pero no `SHA256SUMS.txt`:

```text
Firma valida: SHA256SUMS.txt fue firmado por MediSoft y no ha sido alterado.
```

## Preguntas de Analisis

### 1.1. ?Cuantos bits cambiaron entre los dos hashes SHA-256? Usen XOR para contarlos. ?Que propiedad demuestra esto?
Al comparar los hashes SHA-256 de las cadenas `"MediSoft-v2.1.0"` y `"medisoft-v2.1.0"` mediante una operacion XOR, se obtuvo que cambiaron 120 bits. Este resultado demuestra la propiedad de efecto avalancha, segun la cual un cambio minimo en la entrada, incluso cambiar una sola letra mayuscula por minuscula, produce una salida completamente distinta en el hash. En una funcion hash criptografica robusta como SHA-256, es esperable que aproximadamente la mitad de los bits cambien, y eso se observa claramente en este experimento.

### 1.2. Con base en la longitud en bits, explica por que MD5 es considerado inseguro para integridad de archivos
MD5 es considerado inseguro para integridad de archivos porque produce hashes de solo 128 bits, lo cual representa un espacio de salida mucho menor que el de algoritmos modernos como SHA-256, que genera 256 bits. Un espacio de salida mas pequeno incrementa la probabilidad de colisiones, es decir, que dos entradas distintas produzcan el mismo hash. Ademas, MD5 tiene vulnerabilidades criptograficas conocidas que permiten construir colisiones de forma practica, por lo que ya no es confiable para verificar integridad en sistemas modernos.

### 5.1 Porque la firma es valida? Que sucede al ejecutar verificar_paquete.py
Si se altera un byte cualquiera de uno de los archivos originales contentivos del ejercicio 3, la firma digital de SHA256SUMS.txt sigue siendo válida puesto que la firma se hace únicamente sobre el contenido del manifiesto SHA256SUMS.txt y no sobre los archivos de datos directamente. Mientras el manifiesto no cambia, su hash SHA-256 sigue siendo el mismo y, por lo tanto, la verificación usando la clave pública también será correcta. La distinción es que cuando se ejecute verificar_paquete.py, el sistema vuelve a calcular el SHA-256 del archivo cambiado y comprueba que es igual al hash almacenado en el manifiesto; dado que el contenido del archivo ya no coincide con el hash registrado de antemano, la verificación de la integridad del archivo fallará. En otras palabras, la firma digital garantiza la integridad y autenticidad del manifiesto y la función verificar_paquete.py comprueba que los archivos del paquete tienen una integridad válida.