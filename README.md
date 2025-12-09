# Generador de Códigos QR Personalizable 📱

Este script de Python permite generar códigos QR de forma rápida y sencilla desde la terminal. Ofrece opciones de personalización para los colores y garantiza una alta corrección de errores.

## 📋 Requisitos

Para ejecutar este proyecto necesitas **Python 3.x** y las siguientes librerías externas:

* `qrcode`: Para generar la estructura del código.
* `pillow` (PIL): Para manipular y guardar la imagen.

### Instalación de dependencias

Ejecuta el siguiente comando en tu terminal para instalar todo lo necesario:

```bash
pip install qrcode[pil]
````

*Nota: Si tienes problemas, puedes instalar `pillow` por separado con `pip install pillow`.*

## 🚀 Cómo usar

1.  Descarga el archivo `generador_qr.py`.
2.  Abre una terminal en la carpeta donde se encuentra el archivo.
3.  Ejecuta el script:

<!-- end list -->

```bash
python generador_qr.py
```

4.  El programa te pedirá los siguientes datos (puedes pulsar **Enter** para usar los valores por defecto):
      * **Texto o URL:** El contenido a codificar.
      * **Nombre del archivo:** El nombre de salida (ej. `mi_qr.png`).
      * **Color del QR:** Color de los cuadros (ej. `black`, `blue`, `#FF0000`).
      * **Color de fondo:** Color del fondo (ej. `white`, `yellow`).

## ⚙️ Características Técnicas

  * **Nivel de Corrección:** Utiliza `ERROR_CORRECT_H` (High), lo que permite que el QR sea legible incluso si hasta un 30% de la imagen está dañada o cubierta.
  * **Formato de Salida:** Imágenes estándar (PNG, JPG, etc., según la extensión que indiques).
  * **Librería Gráfica:** Utiliza `PIL` (Python Imaging Library) para el renderizado de colores personalizados.

## 📄 Ejemplo de Ejecución

```text
Introduce el texto o URL: google.com
Nombre del archivo (default: mi_qr.png): google.png
Color del QR (default: black): blue
Color de fondo (default: white): white
Código QR guardado como: google.png
```
