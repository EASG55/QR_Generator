import qrcode
from PIL import Image

def generar_qr_code(datos, nombre_archivo='qr_code.png', 
                    color_relleno='black', color_fondo='white'):
    """
    Genera un código QR personalizado
    
    :param datos: Texto o URL a codificar
    :param nombre_archivo: Nombre del archivo de salida
    :param color_relleno: Color del QR (default: negro)
    :param color_fondo: Color de fondo (default: blanco)
    """
    # Configurar el código QR
    qr = qrcode.QRCode(
        version=1,  # Tamaño (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Corrección de errores alta
        box_size=10,  # Tamaño de cada caja
        border=5  # Grosor del borde
    )
    
    # Añadir datos
    qr.add_data(datos)
    qr.make(fit=True)
    
    # Crear imagen
    img = qr.make_image(fill_color=color_relleno, back_color=color_fondo)
    
    # Guardar
    img.save(nombre_archivo)
    print(f"Código QR guardado como: {nombre_archivo}")
    return img

# Uso del generador
if __name__ == "__main__":
    url = input("Introduce el texto o URL: ")
    archivo = input("Nombre del archivo (default: mi_qr.png): ") or "mi_qr.png"
    color_qr = input("Color del QR (default: black): ") or "black"
    color_bg = input("Color de fondo (default: white): ") or "white"
    
    generar_qr_code(url, archivo, color_qr, color_bg)
