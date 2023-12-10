from PIL import Image
def extraer_datos(imagen_con_datos_ocultos):
    img = Image.open(imagen_con_datos_ocultos)
    datos_binarios = ""
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            # Extrae el bit menos significativo de cada componente de color
            for c in range(3):  # R, G, B
                datos_binarios += str(pixel[c] & 1)
    # Convierte los bits a caracteres ASCII
    datos_extraidos = ''.join([chr(int(datos_binarios[i:i+8], 2)) for i in range(0, len(datos_binarios), 8)])
    return datos_extraidos
# Ejemplo de uso
imagen_con_datos_ocultos = "hack_set.png"
mensaje_extraido = extraer_datos(imagen_con_datos_ocultos)
print("Mensaje oculto en la imagen:", mensaje_extraido)
