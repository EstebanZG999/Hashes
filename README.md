# Laboratorio de Hashes

## Descripción del Proyecto

Este proyecto implementa distintos mecanismos basados en funciones hash para un escenario de seguridad aplicado a la empresa ficticia MediSoft S.A., la cual distribuye software de diagnóstico a hospitales en Centroamérica.

El laboratorio cubre cinco áreas principales:

- comparación de algoritmos hash;
- consulta de contraseñas comprometidas;
- verificación de integridad de archivos mediante SHA-256;
- firma digital de manifiestos con RSA;
- validación de autenticidad usando clave pública.

El objetivo es demostrar, tanto de forma práctica como conceptual, cómo se utilizan los hashes y las firmas digitales para proteger la integridad de paquetes distribuidos y el almacenamiento seguro de credenciales.

## Objetivos de Aprendizaje

- Explicar las propiedades fundamentales de las funciones hash: unidireccionalidad, determinismo, efecto avalancha y resistencia a colisiones.
- Seleccionar el algoritmo hash correcto según el caso de uso: SHA-256 para integridad, Argon2id para contraseñas, HMAC-SHA256 para autenticación de mensajes.
- Implementar verificación de integridad de archivos usando SHA-256 con Python.
- Demostrar experimentalmente por qué MD5 y SHA-1 no deben usarse en sistemas modernos.
- Implementar mecanismos seguros para autenticidad e integridad de artefactos distribuidos.
- Diseñar y ejecutar pruebas automatizadas con `pytest`.

## Estructura del Proyecto

```text
Hashes/
├── README.md
├── explorar_hashes.py
├── consultar_hibp.py
├── generar_manifiesto.py
├── verificar_paquete.py
├── generar_claves_rsa.py
├── firmar_manifiesto.py
├── verificar_firma.py
├── SHA256SUMS.txt
├── SHA256SUMS.sig
├── medisoft_priv.pem
├── medisoft_pub.pem
└── tests/
```

## Requisitos

- Python 3.10 o superior
- `pip`
- `pytest`
- `pycryptodome`

## Instalación

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
pip install -r requirements.txt
```

## Uso

### 1. Comparación de algoritmos hash

```bash
python explorar_hashes.py
```

### 2. Consulta de contraseñas en HIBP

```bash
python consultar_hibp.py
```

### 3. Generación del manifiesto de integridad

```bash
python generar_manifiesto.py <archivo1> <archivo2> <archivo3> <archivo4> <archivo5>
```

### 4. Verificación del paquete

```bash
python verificar_paquete.py SHA256SUMS.txt
```

### 5. Generación de claves RSA

```bash
python generar_claves_rsa.py
```

### 6. Firma digital del manifiesto

```bash
python firmar_manifiesto.py
```

### 7. Verificación de firma digital

```bash
python verificar_firma.py
```

### 8. Ejecución de pruebas

```bash
pytest
```

## Ejemplos de Ejecución

### Ejemplo 1. Salida de `explorar_hashes.py`

### Ejemplo 2. Salida de `consultar_hibp.py`

### Ejemplo 3. Salida de `generar_manifiesto.py`

### Ejemplo 4. Salida de `verificar_paquete.py`

### Ejemplo 5. Salida de `generar_claves_rsa.py`

### Ejemplo 6. Salida de `firmar_manifiesto.py`

### Ejemplo 7. Salida de `verificar_firma.py`

### Ejemplo 8. Salida de `pytest`

## Preguntas de Análisis

### 1.1. ¿Cuántos bits cambiaron entre los dos hashes SHA-256? Usen XOR para contarlos. ¿Qué propiedad demuestra esto?
Al comparar los hashes SHA-256 de las cadenas "MediSoft-v2.1.0" y "medisoft-v2.1.0", se pudo ver que al final de todo el procedimiento fueron 120 bits los que cambiaron. Este cambio demuestra lo que vimos en clase, la propiedad avalancha, que establece que al tener un pequeño cambio en la entrada, produce una salida totalmente diferente en el hash. En funciones como la funcion SHA-256, se espera que aproximadamente la mitad de los bits cambien, lo cual se cumple en este caso. 

### 1.2. Con base en la longitud en bits, explica por qué MD5 es considerado inseguro para integridad de archivos 
MD5 es considerado inseguro para garantizar la integridad de archivos principalmente debido a que produce hashes de solo 128 bits El MD5 es cosiderado inseguro para la integridad de archvos debido a que su funcion de hash solo produce hashes de 128 bits, lo cual es la mitad de lo que representa la salida de un algoritmo como el SHA-256, lo cual es un espacio de salida menor en comparación con algoritmos modernos como SHA-256. Esta salida menor significa que dos entradas distintas tiene mayor probabilidad de generar un mismo hash. Además, MD5 presenta vulnerabilidades criptográficas conocidas que permiten generar colisiones de forma intencional, lo cual compromete directamente su confiabilidad.

### 3. ¿Qué demuestra la consulta a HIBP sobre el uso de contraseñas comunes?

### 4. ¿Por qué aplicar SHA-256 directamente a una contraseña no se considera una práctica segura para almacenamiento de credenciales?

### 5. ¿Qué ventaja aporta publicar un manifiesto `SHA256SUMS.txt` junto con los archivos distribuidos?

### 6. ¿Qué sucede cuando se modifica un byte de un archivo después de haber generado el manifiesto?

### 7. ¿Por qué un atacante podría reemplazar también el archivo `SHA256SUMS.txt` si el servidor fue comprometido?

### 8. ¿Qué problema resuelve la firma digital del manifiesto?

### 9. ¿Qué ocurre al cambiar un carácter dentro de `SHA256SUMS.txt` y luego verificar la firma?

### 10. Si se modifica un archivo del paquete pero no el manifiesto firmado, ¿por qué la firma puede seguir siendo válida y qué debería reportar `verificar_paquete.py`?

## Pruebas

En esta sección se documentarán las pruebas automatizadas implementadas con `pytest`, así como los escenarios cubiertos por cada una.

## Conclusiones

En esta sección se resumirán los hallazgos del laboratorio, las decisiones de diseño y las lecciones de seguridad obtenidas.
